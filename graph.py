import gtk
import gobject
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg \
	import FigureCanvasGTKAgg as FigureCanvas
import time
import psutil as p

def prepare_cpu_usage():
	t = p.cpu_times()
	if hasattr(t, "nice"):
		return[t.user, t.nice, t.system, t.idle]
	else:
		return [t.user, 0,  t.system, t.idle]


def get_cpu_usage():
        
	global before,i
	
	now = prepare_cpu_usage()

	delta = [now[i]-before[i] for i in range(len(now))]
	total = sum(delta)
	before = now
	return [(100.0*dt)/total for dt in delta]


def update_draw(*args):
	global i
	
	result = get_cpu_usage()

	user.append(result[0])
	nice.append(result[1])
	sys.append(result[2])
	idle.append(result[3])
	
	l_user.set_data(range(len(user)), user)
	l_nice.set_data(range(len(nice)), nice)
	l_sys.set_data(range(len(sys)), sys)
	l_idle.set_data(range(len(idle)), idle)

	fig.canvas.draw()

	i += 1
	if i > 60:
		return False
	else:
		time.sleep(1)
		
	return True
	i = 0

before = prepare_cpu_usage()
win = gtk.Window()
win.connect("destroy", gtk.main_quit)
win.set_default_size(600, 400)
win.set_title("60 Seconds of CPU Usage Updated in real-time")

fig = Figure()
ax = fig.add_subplot(111)

ax.set_xlim(0, 60)
ax.set_ylim([0, 100])

ax.set_autoscale_on(False)

user, nice, sys, idle, = [], [], [], []

l_user, = ax.plot ([], user, label="User %")
l_nice, = ax.plot ([], nice, label="Nice %")
l_sys, = ax.plot([], sys, label="Sys %")
l_idle, = ax.plot([], idle, label="Idle %")

ax.legend()
canvas = FigureCanvas(fig)
win.add(canvas)

update_draw()

gobject.idle_add(update_draw)
win.show_all()

gtk.main()
