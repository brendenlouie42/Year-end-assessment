# python code
#
# script_name: Intro Script
#
# author: The EarSketch Team
#
# description: This code adds one audio clip to the DAW
#
#
#

#Setup Section
from earsketch import *
init()
setTempo(180)

#Music Section

fitMedia(YG_TRAP_BASS_1, 2, 1, 9)

fitMedia(RD_TRAP_SUBBASS_2, 3, 1, 9)



setTempo(120)
fitMedia(RD_TRAP_MAIN808_BEAT_3, 5, 5, 9)

#Finish Section
finish()