# Written by Abhijeet Parida(abhijeet.parida@tum.de)

from matplotlib.pyplot import figure, subplot, plot, title, xlabel, ylabel,legend
from numpy import arange,exp

def plotter_exp(p_exp,dt_all,tend,labels):
    import matplotlib.pyplot as plt
    figure()


    ##subplot for dt=1/2
    dt=dt_all[0]
    subplot(2, 2, 1)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 10/(1+(9*exp(-tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/4
    dt=dt_all[1]
    subplot(2, 2, 2)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 10/(1+(9*exp(-tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/8
    dt=dt_all[2]
    subplot(2, 2, 3)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 10/(1+(9*exp(-tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/16
    dt=dt_all[3]
    subplot(2, 2, 4)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 10/(1+(9*exp(-tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])
    plt.show
    return

def plotter_imp(p_exp,dt_all,tend,labels):
    import matplotlib.pyplot as plt
    figure()


    ##subplot for dt=1/2
    dt=dt_all[0]
    subplot(2, 2, 1)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 200/(20-(10*exp(-7*tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/4
    dt=dt_all[1]
    subplot(2, 2, 2)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 200/(20-(10*exp(-7*tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/8
    dt=dt_all[2]
    subplot(2, 2, 3)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 200/(20-(10*exp(-7*tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])

    ##subplot for dt=1/16
    dt=dt_all[3]
    subplot(2, 2, 4)
    t = arange(0,tend,dt)
    tip = arange(0,tend,dt_all[-1])
    p = 200/(20-(10*exp(-7*tip)))
    title("function p(t) v/s t for dt="+str(dt))
    xlabel("t")
    ylabel("p(t)")
    handle1,=plot(tip,p,'b',label='Analytic Soln')
    handle2,=plot(t,p_exp[dt],'r',label=labels)
    legend(handles=[handle1,handle2])
    plt.show()

    return


