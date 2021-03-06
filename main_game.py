#3rd party modules
import libtcodpy as libtcod
import pygame

#game files
import constants



#      _______.___________..______       __    __    ______ .___________.
#     /       |           ||   _  \     |  |  |  |  /      ||           |
#    |   (----`---|  |----`|  |_)  |    |  |  |  | |  ,----'`---|  |----`
#     \   \       |  |     |      /     |  |  |  | |  |         |  |     
# .----)   |      |  |     |  |\  \----.|  `--'  | |  `----.    |  |     
# |_______/       |__|     | _| `._____| \______/   \______|    |__|         

class struc_Tile:
	def __init__(self, block_path):
		self.block_path = block_path                                                                       





# .___  ___.      ___      .______   
# |   \/   |     /   \     |   _  \  
# |  \  /  |    /  ^  \    |  |_)  | 
# |  |\/|  |   /  /_\  \   |   ___/  
# |  |  |  |  /  _____  \  |  |      
# |__|  |__| /__/     \__\ | _|     

def map_create():
	new_map = [[ struc_Tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH) ]

	new_map[10][10].block_path = True
	new_map[10][15].block_path = True

	return new_map
                                   





# _______  .______          ___   ____    __    ____  __  .__   __.   _______ 
# |       \ |   _  \        /   \  \   \  /  \  /   / |  | |  \ |  |  /  _____|
# |  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  |  | |   \|  | |  |  __  
# |  |  |  ||      /      /  /_\  \  \            /   |  | |  . `  | |  | |_ | 
# |  '--'  ||  |\  \----./  _____  \  \    /\    /    |  | |  |\   | |  |__| | 
# |_______/ | _| `._____/__/     \__\  \__/  \__/     |__| |__| \__|  \______| 
                                                                             
def draw_game():

	#clear the surface
	SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

	#draw the map
	draw_map(GAME_MAP)
	#draw the character
	SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200))

	# update the display
	pygame.display.flip()

def draw_map(map_to_draw):

	for x in range(0,constants.MAP_WIDTH):
		for y in range(0,constants.MAP_HEIGHT):
			if map_to_draw[x][y].block_path == True:
				#draw wall
				SURFACE_MAIN.blit(constants.S_WALL, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))
			else:
				SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))
#   _______      ___      .___  ___.  _______ 
#  /  _____|    /   \     |   \/   | |   ____|
# |  |  __     /  ^  \    |  \  /  | |  |__   
# |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
# |  |__| |  /  _____  \  |  |  |  | |  |____ 
#  \______| /__/     \__\ |__|  |__| |_______|
                                           
def game_main_loop():
	'''In this function, we loop the main game'''
	game_quit = False

	while not game_quit:

		#get player input
		events_list = pygame.event.get()

		#TODO process input
		for event in events_list:
			if event.type == pygame.QUIT:
				game_quit = True

		# draw the game
		draw_game()

	#quit the game
	pygame.quit()
	exit()

def game_initialize():
	'''This function initializes the main window, and pygame'''

	global SURFACE_MAIN, GAME_MAP

	#initialize pygame
	pygame.init()

	SURFACE_MAIN = pygame.display.set_mode( (constants.GAME_WIDTH, constants.GAME_HEIGHT) )

	GAME_MAP = map_create()




#            ::'.:                       
#             ''M;                       
#             """:;                       
#                 M;.     .               
#        ...... ..M:'    MM;.             
#      ;MMMMMMMMMM:     :MMMM.           
#      MMMMMMMMMMMMM..  ;MMMM;.           
#      'MMMMMMMMMMMMMM;.MMM'MM;           
#       '"MMMMMMMMMMMMMMMMM 'MM;     ,. . 
# , ,:    ':MMMMMMMMMMMMMMM  'MM.   :;'"" 
# "'.:     :M:":MMMMMMMMMMM   'M; ,;:;;"" 
# '"'M;..;.;M'  ""MMMMMMMM:    'M.MMMM:"" 
# '"'  ""'""" ;.MMMMMMMM""      '"""'     
#          ,;MMMMMMM:""                   
#          'MMMMMMM;.;.                   
#             """'""""":M..               
#                       ,MM               
#   -hrr-              ;MM:               
#                    ,;'MM'               
#                    ":"M:               
#                    ::::.  
##EXECUTE GAME##
if __name__ == '__main__':
	game_initialize()
	game_main_loop()