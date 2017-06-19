from earsketch import *

init()
setTempo (78)
fitMedia (Y21_DRUMPAD_1, 1,1,50)

fitMedia (HIPHOP_BASSSUB_003, 2,4,20)

fitMedia (YG_NEW_HIP_HOP_SNARE_6, 3,20,20.25)


beat1 = "0--0-0--0-0--0-0--0-0--0" 

for measure in range(1,4):
  bass = RD_TRAP_MAIN808_BEAT_2
  
  makeBeat(bass, 6, measure, beat1)
  

fitMedia (HIPHOP_BASSSUB_003, 4,20.25,50)


fitMedia(Y21_DRUMPAD_1, 1, 1, 5)
fitMedia(HIPHOP_BASSSUB_003, 2, 1, 5) 
for measure in range(1, 5):
	fitMedia(HIPHOP_BASSSUB_003, 3, measure, measure + 1) 
	
fitMedia(RD_TRAP_MAIN808_BEAT_2, 1, 25, 40)
fitMedia(HIPHOP_BASSSUB_003, 2, 25, 40) 
for measure in range(1, 5):
	fitMedia(HIPHOP_BASSSUB_003, 3, measure, measure + 1) 

setEffect(4, DELAY, DELAY_TIME, 500)


for RD_TRAP_DRUM_PART_24 in range(4):
 finish()