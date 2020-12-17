from moviepy.editor import VideoFileClip
import sys 

if len(sys.argv) < 2 :
	print("Usage : python videotogif_cml.py [video_path] [fps] [time_start] [time_end] [resize_to] [ouput_path]")
	sys.exit()
else:
	print("Start converting...")
	videoclip = VideoFileClip( sys.argv[1])

	fps = 10

	if len(sys.argv) > 2:
		fps = int(sys.argv[2])

	if len(sys.argv) > 4:
		time_start = float(sys.argv[3])
		time_end = float(sys.argv[4])
		videoclip = videoclip.subclip(time_start,time_end)
		
	elif len(sys.argv) > 3:
		time_start = float(sys.argv[3])
		videoclip = videoclip.subclip(time_start)
		
	if len(sys.argv) > 5:
		videoclip = videoclip.resize(float(sys.argv[5]))
	
	output_path = "output.gif"

	if len(sys.argv) > 6:
		output_path = sys.argv[6]

	videoclip.write_gif(output_path, fps=fps)
	
	

	
	

