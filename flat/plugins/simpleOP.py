# -*- coding: utf-8 -*-
import time

def on_info(server, info):
	waiting_time=10	# 在这里设置重启或关服等待的时间
	time_left=waiting_time
	if info.is_player and info.content == '!!op':
		server.execute('op ' + info.player)

	if info.is_player and info.content == '!!deop':
		server.execute('deop ' + info.player)

	if info.content == '!!restart':
		restart_message=''
		while True:
			restart_message='Server will restart in {} second(s), please save your work!'.format(time_left)
			server.say(restart_message)
			if(time_left==0):
				server.restart()
				break
			else:
				time.sleep(1)
				time_left=time_left-1

	if info.content == '!!stop':
		stop_message=''
		while True:
			stop_message='Server will close in {} second(s), please save your work!'.format(time_left)
			server.say(stop_message)
			if(time_left==0):
				server.stop_exit()
				break
			else:
				time.sleep(1)
				time_left=time_left-1
