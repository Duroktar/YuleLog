from __future__ import print_function
from asciimatics.renderers import FigletText, Fire, ColourImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print, Snow, Cycle
from asciimatics.exceptions import ResizeScreenError
from pyfiglet import Figlet
import os, sys

YULE_LOG = ["""                                                                        .:'#'.         
                                                          `.,;;'+#@#####++++++#@;      
                                           .,::;'+#@@######++++++++++++++++++++++@'    
                       ````..:;+###@@@@@###+++++++++++++++++++++++++++++###+++++++#@`  
     .;++#######@@@###+++++++++++++++++++++++++++++++++++++#####++++++++++++++++++++#. 
   '+,`.,;@#+++++++++++++++++++++++++++++#############++++++++++++++++++++++++++++++#+`
 `#.:#+'#+.`'@++++#############+++++++++++++++++++++++++++++++++++++++++###++++++++++#:
 #:#:,+;#.'#`.##++++++++++++++++++++++++++++++++++++++++++++++++++####+++++++++++++++#+
;+;',:;,;:;,#,`+#+++++++++++++++###########################+++++++++++++++++++++++++++@
#;'.:'.``,':,+.`##+++++++++++++++++++++++++++++++++++++++++++++++++++#####+++++++++++##
@;+.:'.```;'`':`,@++++++++++++++++++++++++++++++++#++++#########+++++++++++++++++++++#'
'';:.;;```:;.:#``@#++#######+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#.
.+;+`:::;'+@''#``'@++++++++++++++++++++++++++++++++++++++++++++######+##+++++++++++##. 
 ;;''`.+;:'.,#@@##@#####@@@@@@@++++++++++++++++++#########+++##################++#@;   
 `+,''``````.#.;@@@@@@@@##+++++++++++++#####+++++##@@####':,```               `..      
  `#,,@;```,@,``;@+++++++#####++++++++##@@##+:.``                                      
    ''``:;;,```;@++++++++++####@@+;:,.                                                 
     .+'.```,'@#####@#+';,.                                                            
        `;##':`                                                                        
"""]

x = YULE_LOG[0].split('\n')
LOG_HEIGHT = len(x)
LOG_LENGTH = len(x[0])
HALF_LOG_HEIGHT = LOG_HEIGHT // 2
HALF_LOG_LENGTH = LOG_LENGTH // 2


def yule_log(screen):
    screen_height = screen.height
    screen_width = screen.width
    log_x = (screen_width // 2) - HALF_LOG_LENGTH
    log_y = (screen_height // 2) + HALF_LOG_HEIGHT
    if screen_height < 30:
        log_y = screen_height // 3
    elif screen_height < 48:
        log_y = screen_height // 2

    scenes = []

    effects = [
        Snow(screen),
        Print(screen,
              Fire(screen.height - 10, 80, "*" * 70, 0.8, 60, screen.colours,
                   bg=screen.colours >= 256),
              0,
              speed=1,
            ),
        Print(screen,
              StaticRenderer(images=YULE_LOG),
              x=log_x,
              y=log_y,
              colour=1,
              speed=1,
              transparent=True),
    ]
    if screen_height > 40:
        effects += [
            Print(
                screen,
                FigletText("MERRY", font='univers'),
                1,
                speed=1,
                start_frame=5),
            Print(
                screen,
                FigletText("CHRISTMAS!", font='univers'),
                10,
                speed=1,
                start_frame=15),
        ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


def main():
    while True:
        try:
            Screen.wrapper(yule_log)
            sys.exit(0)
        except ResizeScreenError:
            pass


if __name__ == "__main__":
    main()
    # -p[hj p[[ hjh[]kj[] k ''[;hjuu]]]]     Hannah 24/12/2016
