from distkv.util import attrdict

CFG = attrdict(
        prefix=('.distkv','gpio'),
        interval=1,     # input/count: Pulse reporting frequency
        count=True,     # input/count, input/button: Pulse direction
                        # up down both=True False None
        low=False,     # if True, he default is active-low
        skip=False,     # ignore signals < t_bounce
        t_idle=1.5,     # input/button: max pulse width
        t_bounce=0.05,  # input/button: min pulse width
    )

