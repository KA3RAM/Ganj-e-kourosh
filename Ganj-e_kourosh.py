import pygame, sys, webbrowser, os
# import pygame.freetype
# import arabic_reshaper
# from bidi.algorithm import get_display
from pygame.locals import *
import time
timer_start = None
pygame.init()

can_q1 = True
can_q2 = True
can_q3 = True
can_q4 = True
can_q5 = True
can_q6 = True
can_q7 = True
can_q8 = True
can_q9 = True
can_q10 = True
# ,,,,,,,,,
can_qc1 = True
can_qc2 = True
can_qc3 = True
can_qc4 = True
can_qc5 = True
can_qc6 = True
can_qc7 = True
can_qc8 = True
can_qc9 = True
can_qc10 = True 
#,,,,,,,,,,,,,,,,,,
can_qcm1 = True
can_qcm2 = True
can_qcm3 = True
can_qcm4 = True
can_qcm5 = True
can_qcm6 = True
can_qcm7 = True
can_qcm8 = True
can_qcm10 = True 
# ,,,,,,,,,,,,,,,,,,
can_qcd1 = True
can_qcd2 = True
can_qcd3 = True
can_qcd4 = True
can_qcd5 = True
can_qcd6 = True
can_qcd7 = True
can_qcd8 = True
can_qcd10 = True 



question_points = 0
menu = 0
black = (0, 0, 0)
yellow = (252, 252, 3)
#Game FPS
fps = 60
clock = pygame.time.Clock()

# Screen settings
win = pygame.display.set_mode((1050, 600))
pygame.display.set_caption("Ganj-e kourosh")

# Icon
icon = pygame.image.load("pictures/icon_game/game_icon.png") 
pygame.display.set_icon(icon)

# Game songs
# -->song of main game
pygame.mixer.music.load("music/57 - Tomb Raider Anniversary - Main Theme by Troels Brun Folmann.mp3")
volume = 0

pygame.mixer.music.play(-1)
# -->song of sound effect
game_sound_effect = pygame.mixer.Sound("music/click_game_effect.mp3")




# تصاویر سوالات
question_images = []
question_images_index = 0
for i in range(1, 10):
    img = pygame.image.load(f"pictures/soldier_questions/q_{i}.png")
    img_trans = pygame.transform.scale(img, (1050, 600))
    question_images.append(img_trans)

question_images_level2 = []
question_images_index_level2 = 0
for i in range(1, 10):
    img = pygame.image.load(f"pictures/prince_questions/qc_{i}.png")
    img_trans = pygame.transform.scale(img, (1050, 600))
    question_images_level2.append(img_trans)

question_images_level3 = []
question_images_index_level3 = 0
for i in range(1, 10):
    img = pygame.image.load(f"pictures/minister_questions/qcpm_{i}.png")
    img_trans = pygame.transform.scale(img, (1050, 600))
    question_images_level3.append(img_trans)


question_images_level4 = []
question_images_index_level4 = 0
for i in range(1, 10):
    img = pygame.image.load(f"pictures/king_questions/darq_{i}.png")
    img_trans = pygame.transform.scale(img, (1050, 600))
    question_images_level4.append(img_trans)


# soldier / playerp
p_1 = pygame.image.load("pictures/dialogs/first_scene/p_1.png")
p_1_trans = pygame.transform.scale(p_1, (1000, 550))

p_2 = pygame.image.load("pictures/dialogs/first_scene/p_2.png")
p_2_trans = pygame.transform.scale(p_2, (1000, 550))

p_3 = pygame.image.load("pictures/dialogs/first_scene/p_3.png")
p_3_trans = pygame.transform.scale(p_3, (1000, 550))

p_4 = pygame.image.load("pictures/dialogs/first_scene/p_4.png")
p_4_trans = pygame.transform.scale(p_4, (1000, 550))

p_5 = pygame.image.load("pictures/dialogs/first_scene/p_5.png")
p_5_trans = pygame.transform.scale(p_5, (1000, 550))

p_6 = pygame.image.load("pictures/dialogs/first_scene/p_6.png")
p_6_trans = pygame.transform.scale(p_6, (1000, 550))

p_7 = pygame.image.load("pictures/dialogs/first_scene/p_7.png")
p_7_trans = pygame.transform.scale(p_7, (1000, 550))

p_8 = pygame.image.load("pictures/dialogs/first_scene/p_8.png")
p_8_trans = pygame.transform.scale(p_8, (1000, 550))

p_9 = pygame.image.load("pictures/dialogs/first_scene/p_9.png")
p_9_trans = pygame.transform.scale(p_9, (1000, 550))

p_10 = pygame.image.load("pictures/dialogs/first_scene/p_10.png")
p_10_trans = pygame.transform.scale(p_10, (1000, 550))

p_11 = pygame.image.load("pictures/dialogs/first_scene/p_11.png")
p_11_trans = pygame.transform.scale(p_11, (1000, 550))

p_12 = pygame.image.load("pictures/dialogs/first_scene/p_12.png")
p_12_trans = pygame.transform.scale(p_12, (1000, 550))



right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))




dialog_images = [p_1_trans, p_2_trans, p_3_trans, p_4_trans, p_5_trans, p_6_trans, p_7_trans,p_8_trans ,p_9_trans, p_10_trans, p_11_trans, p_12_trans]
dialog_index = 0
dialog_start_time = None

# prince questions
pc_1 = pygame.image.load("pictures/dialogs/sec_scene/qc_1.png")
pc_1_trans = pygame.transform.scale(pc_1, (1000, 550))

pc_2 = pygame.image.load("pictures/dialogs/sec_scene/qc_2.png")
pc_2_trans = pygame.transform.scale(pc_2, (1000, 550))

pc_3 = pygame.image.load("pictures/dialogs/sec_scene/qc_3.png")
pc_3_trans = pygame.transform.scale(pc_3, (1000, 550))

pc_4 = pygame.image.load("pictures/dialogs/sec_scene/qc_4.png")
pc_4_trans = pygame.transform.scale(pc_4, (1000, 550))

pc_5 = pygame.image.load("pictures/dialogs/sec_scene/qc_5.png")
pc_5_trans = pygame.transform.scale(pc_5, (1000, 550))

pc_6 = pygame.image.load("pictures/dialogs/sec_scene/qc_6.png")
pc_6_trans = pygame.transform.scale(pc_6, (1000, 550))

pc_7 = pygame.image.load("pictures/dialogs/sec_scene/qc_7.png")
pc_7_trans = pygame.transform.scale(pc_7, (1000, 550))

pc_8 = pygame.image.load("pictures/dialogs/sec_scene/qc_8.png")
pc_8_trans = pygame.transform.scale(pc_8, (1000, 550))

pc_9 = pygame.image.load("pictures/dialogs/sec_scene/qc_9.png")
pc_9_trans = pygame.transform.scale(pc_9, (1000, 550))

pc_10 = pygame.image.load("pictures/dialogs/sec_scene/qc_10.png")
pc_10_trans = pygame.transform.scale(pc_10, (1000, 550))




dialog_images_level2 = [pc_1_trans, pc_2_trans, pc_3_trans, pc_4_trans, pc_5_trans, pc_6_trans, pc_7_trans,pc_8_trans ,pc_9_trans, pc_10_trans]
dialog_index_level2 = 0
dialog_start_time_level2 = None





# minister questions
pc_1 = pygame.image.load("pictures/dialogs/therd_scene/qcp_1.png")
pc_1_trans = pygame.transform.scale(pc_1, (1000, 550))

pc_2 = pygame.image.load("pictures/dialogs/therd_scene/qcp_2.png")
pc_2_trans = pygame.transform.scale(pc_2, (1000, 550))

pc_3 = pygame.image.load("pictures/dialogs/therd_scene/qcp_3.png")
pc_3_trans = pygame.transform.scale(pc_3, (1000, 550))

pc_4 = pygame.image.load("pictures/dialogs/therd_scene/qcp_4.png")
pc_4_trans = pygame.transform.scale(pc_4, (1000, 550))

pc_5 = pygame.image.load("pictures/dialogs/therd_scene/qcp_5.png")
pc_5_trans = pygame.transform.scale(pc_5, (1000, 550))

pc_6 = pygame.image.load("pictures/dialogs/therd_scene/qcp_6.png")
pc_6_trans = pygame.transform.scale(pc_6, (1000, 550))

pc_7 = pygame.image.load("pictures/dialogs/therd_scene/qcp_7.png")
pc_7_trans = pygame.transform.scale(pc_7, (1000, 550))

pc_8 = pygame.image.load("pictures/dialogs/therd_scene/qcp_8.png")
pc_8_trans = pygame.transform.scale(pc_8, (1000, 550))

pc_9 = pygame.image.load("pictures/dialogs/therd_scene/qcp_9.png")
pc_9_trans = pygame.transform.scale(pc_9, (1000, 550))

pc_10 = pygame.image.load("pictures/dialogs/therd_scene/qcp_10.png")
pc_10_trans = pygame.transform.scale(pc_10, (1000, 550))

pc_11 = pygame.image.load("pictures/dialogs/therd_scene/qcp_11.png")
pc_11_trans = pygame.transform.scale(pc_10, (1000, 550))

pc_12 = pygame.image.load("pictures/dialogs/therd_scene/qcp_12.png")
pc_12_trans = pygame.transform.scale(pc_12, (1000, 550))

pc_13 = pygame.image.load("pictures/dialogs/therd_scene/qcp_13.png")
pc_13_trans = pygame.transform.scale(pc_13, (1000, 550))





dialog_images_level3 = [pc_1_trans, pc_2_trans, pc_3_trans, pc_4_trans, pc_5_trans, pc_6_trans, pc_7_trans,pc_8_trans ,pc_9_trans, pc_10_trans, pc_11_trans, pc_12_trans, pc_13_trans, pc_2_trans]
dialog_index_level3 = 0
dialog_start_time_level3 = None




# minister questions
pc_1 = pygame.image.load("pictures/dialogs/four_scene/dar_1.png")
pc_1_trans = pygame.transform.scale(pc_1, (1000, 550))

pc_2 = pygame.image.load("pictures/dialogs/four_scene/dar_2.png")
pc_2_trans = pygame.transform.scale(pc_2, (1000, 550))

pc_3 = pygame.image.load("pictures/dialogs/four_scene/dar_3.png")
pc_3_trans = pygame.transform.scale(pc_3, (1000, 550))

pc_4 = pygame.image.load("pictures/dialogs/four_scene/dar_4.png")
pc_4_trans = pygame.transform.scale(pc_4, (1000, 550))

pc_5 = pygame.image.load("pictures/dialogs/four_scene/dar_5.png")
pc_5_trans = pygame.transform.scale(pc_5, (1000, 550))

pc_6 = pygame.image.load("pictures/dialogs/four_scene/dar_6.png")
pc_6_trans = pygame.transform.scale(pc_6, (1000, 550))

pc_7 = pygame.image.load("pictures/dialogs/four_scene/dar_7.png")
pc_7_trans = pygame.transform.scale(pc_7, (1000, 550))

pc_8 = pygame.image.load("pictures/dialogs/four_scene/dar_8.png")
pc_8_trans = pygame.transform.scale(pc_8, (1000, 550))

pc_9 = pygame.image.load("pictures/dialogs/four_scene/dar_9.png")
pc_9_trans = pygame.transform.scale(pc_9, (1000, 550))

pc_10 = pygame.image.load("pictures/dialogs/four_scene/dar_10.png")
pc_10_trans = pygame.transform.scale(pc_10, (1000, 550))

pc_11 = pygame.image.load("pictures/dialogs/four_scene/dar_11.png")
pc_11_trans = pygame.transform.scale(pc_11, (1000, 550))






dialog_images_level4 = [pc_1_trans, pc_2_trans, pc_3_trans, pc_4_trans, pc_5_trans, pc_6_trans, pc_7_trans,pc_8_trans ,pc_9_trans, pc_10_trans, pc_11_trans, pc_2_trans]
dialog_index_level4 = 0
dialog_start_time_leve4 = None




#game maps
first_game_map = pygame.image.load("pictures/maps/first_gm.jpg")
transform_first_game_map = pygame.transform.scale(first_game_map, (1050, 600))

second_game_map = pygame.image.load("pictures/maps/map_level2.jpg")
transform_first_game_map_level2 = pygame.transform.scale(second_game_map, (1050, 600))

therd_game_map = pygame.image.load("pictures/maps/last_map.jpg")
transform_first_game_map_level3 = pygame.transform.scale(therd_game_map, (1050, 600))

# credits
finish = pygame.image.load("pictures/maps/finisher.jpg")
trans_finish = pygame.transform.scale(finish, (1050, 600))



#  Sound effect playing
def sound_effect ():
    game_sound_effect.play()

# _________________________________________________GAME MAPS_________________________________________________#
# Main menu
def main_menu():
    main_menu_image = pygame.image.load("pictures/maps/mainmenu_image.jpg")
    transform_main_menu_image = pygame.transform.scale(main_menu_image, (1050, 600))

    setting_icon = pygame.image.load("pictures/svg/setting_icon.png")
    transform_setting_icon = pygame.transform.scale(setting_icon, (65, 65))

    question_icon = pygame.image.load("pictures/svg/question_icon.png")
    transform_question_icon = pygame.transform.scale(question_icon, (65, 65))

    win.blit(transform_main_menu_image, (0, 0))
    win.blit(transform_setting_icon, (10, 10))
    win.blit(transform_question_icon, (85, 13))

    pygame.draw.rect(win, yellow, pygame.Rect(435, 215, 175, 75),  4, 20)

# setting
def setting():
    setting_image = pygame.image.load("pictures/maps/setting_back.jpg")
    transform_setting_image = pygame.transform.scale(setting_image, (1050, 600))

    exit_image = pygame.image.load("pictures/svg/icon-exit-13.jpg")
    transform_exit_image = pygame.transform.scale(exit_image, (60, 60))
    
    aboutus_image = pygame.image.load("pictures/svg/about_us.png")
    transform_aboutus_image = pygame.transform.scale(aboutus_image, (60, 60))

    plus_image = pygame.image.load("pictures/svg/Plus_green-512.png")
    transform_plus_image = pygame.transform.scale(plus_image, (50, 50))

    minus_image = pygame.image.load("pictures/svg/minus.png")
    transform_minus_image = pygame.transform.scale(minus_image, (50, 50))

    mute_image = pygame.image.load("pictures/svg/mute.png")
    transform_mute_image = pygame.transform.scale(mute_image, (50, 50))

    unmute_image = pygame.image.load("pictures/svg/sound.png")
    transform_unmute_image = pygame.transform.scale(unmute_image, (50, 50))

    win.blit(transform_setting_image, (0, 0))
    win.blit(transform_unmute_image, (820, 115))
    win.blit(transform_mute_image, (750, 115))
    win.blit(transform_exit_image, (820, 275))
    win.blit(transform_aboutus_image, (750, 190))
    win.blit(transform_plus_image, (680, 115))
    win.blit(transform_minus_image, (620, 115))

# game info
def info1():
    info1_image = pygame.image.load("pictures/info_dialogs/1.png")
    transform_info1_image = pygame.transform.scale(info1_image, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    win.blit(transform_info1_image, (0,0))
    win.blit(transform_right_arrow, (950, 70))
def info2():
    info2_image = pygame.image.load("pictures/info_dialogs/2.png")
    transform_info2_image = pygame.transform.scale(info2_image, (1050, 600))


    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    win.blit(transform_info2_image, (0,0))
    win.blit(transform_right_arrow, (950, 150))
def info3():
    info3_image = pygame.image.load("pictures/info_dialogs/3.png")
    transform_info3_image = pygame.transform.scale(info3_image, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    win.blit(transform_info3_image, (0,0))
    win.blit(transform_right_arrow, (950, 230))
def info4():
    info4_image = pygame.image.load("pictures/info_dialogs/4.png")
    transform_info4_image = pygame.transform.scale(info4_image, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    win.blit(transform_info4_image, (0,0))
    win.blit(transform_right_arrow, (950, 310))
def info5():
    info5_image = pygame.image.load("pictures/info_dialogs/5.png")
    transform_info5_image = pygame.transform.scale(info5_image, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    win.blit(transform_info5_image, (0,0))
    win.blit(transform_right_arrow, (950, 390))
def info6():
    info6_image = pygame.image.load("pictures/info_dialogs/6.png")
    transform_info6_image = pygame.transform.scale(info6_image, (1050, 600))

    win.blit(transform_info6_image, (0,0))

#  Game map
def first_entering_to_game():
    player_enters = pygame.image.load("pictures/maps/first_entering.jpg")
    transform_player_enters = pygame.transform.scale(player_enters, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))


    win.blit(transform_player_enters, (0,0))
    win.blit(transform_right_arrow, (950, 230))

def level_one():
    level1_back_image = pygame.image.load("pictures/maps/running_people.png")
    transform_level1_back_image = pygame.transform.scale(level1_back_image, (1050, 600))

    win.blit(transform_level1_back_image, (0, 0))

def level_two():
    level2_back_image = pygame.image.load("pictures/maps/girl_home.jpg")
    transform_level2_back_image = pygame.transform.scale(level2_back_image, (1050, 600))
    win.blit(transform_level2_back_image, (0, 0))

# level 3:
level3_back_image = pygame.image.load("pictures/maps/dark_map_under.jpg")
transform_level3_back_image = pygame.transform.scale(level3_back_image, (1050, 600))
level3_back_image2 = pygame.image.load("pictures/maps/light_map_under.jpeg")
transform_level3_back_image2 = pygame.transform.scale(level3_back_image2, (1050, 600))

def level_four():
    level4_back_image = pygame.image.load("pictures/maps/last.webp")
    transform_level4_back_image = pygame.transform.scale(level4_back_image, (1050, 600))
    win.blit(transform_level4_back_image, (0, 0))

# ending
def last():
    moving = pygame.image.load("pictures/maps/finding.webp")
    trans_moving = pygame.transform.scale(moving, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))


    win.blit(trans_moving, (0,0))
    win.blit(transform_right_arrow, (950, 130))

def last2():
    deep_chest = pygame.image.load("pictures/maps/under_chest_top.png")
    trans_deep_chest = pygame.transform.scale(deep_chest, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))


    win.blit(trans_deep_chest, (0,0))
    win.blit(transform_right_arrow, (950, 230))

def last3():
    deep_chest_near = pygame.image.load("pictures/maps/under_chest_back.png")
    trans_deep_chest_near = pygame.transform.scale(deep_chest_near, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))


    win.blit(trans_deep_chest_near, (0,0))
    win.blit(transform_right_arrow, (950, 330))


def ending_1():
    ending_1 = pygame.image.load("pictures/maps/finish_1.png")
    transform_finish_1 = pygame.transform.scale(ending_1, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))

    

    win.blit(transform_finish_1, (0,0))
    win.blit(transform_right_arrow, (950, 230))

def ending_2():
    ending_2 = pygame.image.load("pictures/maps/finish_2.png")
    transform_finish_2 = pygame.transform.scale(ending_2, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))



    win.blit(transform_finish_2, (0,0))
    win.blit(transform_right_arrow, (950, 230))

def ending_3():
    ending_3 = pygame.image.load("pictures/maps/finish_3.png")
    transform_finish_3 = pygame.transform.scale(ending_3, (1050, 600))

    right_arrow = pygame.image.load("pictures/svg/right_arrow.png")
    transform_right_arrow = pygame.transform.scale(right_arrow, (100, 70))


    win.blit(transform_finish_3, (0,0))
    win.blit(transform_right_arrow, (950, 230))
# Characters
def king():
    kamandar = pygame.image.load("pictures/characters/king.png")
    transform_kamandar = pygame.transform.scale(kamandar, (250, 250))
    win.blit(transform_kamandar, (800, 350))

def minister():
    kamandar = pygame.image.load("pictures/characters/minister.png")
    transform_kamandar = pygame.transform.scale(kamandar, (300, 300))
    win.blit(transform_kamandar, (750, 320))

def kamandar():
    kamandar = pygame.image.load("pictures/characters/soldier.png")
    transform_kamandar = pygame.transform.scale(kamandar, (330, 330))
    win.blit(transform_kamandar, (730, 350))

def prince():
    kamandar = pygame.image.load("pictures/characters/prince.png")
    transform_kamandar = pygame.transform.scale(kamandar, (260, 260))
    win.blit(transform_kamandar, (800, 350))

def player():
    player = pygame.image.load("pictures/characters/player.png")
    transform_player = pygame.transform.scale(player, (370, 250))
    win.blit(transform_player, (-65, 350))

overlay = pygame.Surface((1050, 600), pygame.SRCALPHA)
overlay.fill((0, 0, 0, 128))
 
home_icon = pygame.image.load("pictures/svg/home_icon.png")
transform_home_icon = pygame.transform.scale(home_icon, (60, 60))







































# def read_data():
#     if os.path.exists("menu_ha"):
#         with open("menu_ha", 'r') as f:
#             try:
#                 menu = f.read().strip()
#             except:
#                 menu = "0"
#     else:
#         menu = "0"

#     if os.path.exists("score_ha"):
#         with open("score_ha", 'r') as f:
#             try:
#                 question_points = int(f.read().strip())
#             except:
#                 question_points = 0
#     else:
#         question_points = 0

#     return question_points, menu

# # تابع برای ذخیره داده‌ها در فایل
# def save_data(name, score):
#     with open("menu_ha", 'w') as f:
#         f.write(str(name))
#     with open("score_ha", 'w') as f:
#         f.write(str(score))

# # شروع برنامه
# question_points, menu= read_data()



font = pygame.font.Font(None, 40)


# Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Event menus
        if menu != 0:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
        if menu == -1:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 820 <= mouse_pos[0] <= 880 and 275 <= mouse_pos[1] <= 335:
                    sound_effect()
                    sys.exit()
                if 750 <= mouse_pos[0] <= 810 and 190 <= mouse_pos[1] <= 250:
                    sound_effect()
                    webbrowser.open(r"https://s6.uupload.ir/files/1_z5yi.png")
                if 820 <= mouse_pos[0] <= 880 and 115 <= mouse_pos[1] <= 165:
                    sound_effect()
                    pygame.mixer.music.unpause()
                if 750 <= mouse_pos[0] <= 800 and 115 <= mouse_pos[1] <= 165:
                    sound_effect()
                    pygame.mixer.music.pause()
                if 620 <= mouse_pos[0] <= 670 and 115 <= mouse_pos[1] <= 165:
                    sound_effect()
                    volume -= 0.3
                    pygame.mixer.music.set_volume(volume)
                if 680 <= mouse_pos[0] <= 730 and 115 <= mouse_pos[1] <= 165:
                    sound_effect()
                    volume += 0.3
                    pygame.mixer.music.set_volume(volume)
             
        if menu == -2:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
            if 950 <= mouse_pos[0] <= 1050 and 70 <= mouse_pos[1] <= 140:
                    sound_effect()
                    menu = -3
        if menu == -3:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
            if 950 <= mouse_pos[0] <= 1050 and 150 <= mouse_pos[1] <= 220:
                    sound_effect()
                    menu = -4
        if menu == -4:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
            if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                    sound_effect()
                    menu = -5
        if menu == -5:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
            if 950 <= mouse_pos[0] <= 1050 and 310 <= mouse_pos[1] <= 390:
                    sound_effect()
                    menu = -6
        if menu == -6:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if 980 <= mouse_pos[0] <= 1040 and 5 <= mouse_pos[1] <= 65:
                    sound_effect()
                    menu = 0
            if 950 <= mouse_pos[0] <= 1050 and 400 <= mouse_pos[1] <= 470:
                    sound_effect()
                    menu = -7

        if menu == 0:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 435 <= mouse_pos[0] <= 610 and 215 <= mouse_pos[1] <= 290:
                    sound_effect()
                    menu = 1

                if 10 <= mouse_pos[0] <= 75 and 10 <= mouse_pos[1] <= 75:
                    sound_effect()
                    menu = -1
                    win.fill(black)

                if 85 <= mouse_pos[0] <= 150 and 13 <= mouse_pos[1] <= 78:
                    sound_effect()
                    menu = -2
                    win.fill(black)

        if menu == 1:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                    sound_effect()
                    menu = 2


# level 1 questions
        if menu == 2000:
                win.blit(question_images[0], (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()         
                        can_q1 = False
                    if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()             
                        can_q1 = False
                    if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()
                        can_q1 = False
                        question_points += 1
                    if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()
                        can_q1 = False

                if can_q1 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2001
                            sound_effect()
                    
        if menu == 2001:
            win.blit(question_images[1], (0, 0))
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q2 = False
                
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q2 = False 
                    question_points += 1
                    
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q2 = False

            if can_q2 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2002
                            sound_effect()
                    
        if menu == 2002:
            win.blit(question_images[2], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q3 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q3 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q3 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q3 = False
                    question_points += 1

            if can_q3 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2003
                            sound_effect()
            
        if menu == 2003:
            win.blit(question_images[3], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q4 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q4 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q4= False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q4 = False

            if can_q4 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2004
                            sound_effect()

        if menu == 2004:
            win.blit(question_images[4], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q5 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q5 = False
                    question_points += 1
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q5 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q5 = False

            if can_q5 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2005
                            sound_effect()

        if menu == 2005:
            win.blit(question_images[5], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q6 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q67= False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q6 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q6 = False

            if can_q6 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2006
                            sound_effect()

        if menu == 2006:
            win.blit(question_images[6], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q7 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q7 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q7 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q7 = False
            if can_q7 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2007
                            sound_effect()

        if menu == 2007:
            win.blit(question_images[7], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_q8 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q8 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q8 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q8 = False

            if can_q8 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2008
                            sound_effect()

        if menu == 2008:
            win.blit(question_images[8], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    question_points += 1
                    can_q9 = False
                    menu = 97
                    
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_q9 = False
                    menu = 97
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_q9 = False
                    menu = 97
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_q9 = False
                    menu = 97

            if can_q9 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 2009
                            sound_effect()
            
# level 2 questions 
        if menu == 3000:
                win.blit(question_images_level2[0], (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()         
                        can_qc1 = False
                        question_points += 1
                    if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()             
                        can_qc1 = False
                    if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()
                        can_qc1 = False
                    if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()
                        can_qc1 = False

                if can_qc1 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3001
                            sound_effect()
                    
        if menu == 3001:
            win.blit(question_images_level2[1], (0, 0))
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc2 = False
                    question_points += 1
                
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc2 = False

            if can_qc2 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3002
                            sound_effect()
                    
        if menu == 3002:
            win.blit(question_images_level2[2], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc3 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc3 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc3 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc3 = False
                    question_points += 1

            if can_qc3 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3003
                            sound_effect()
            
        if menu == 3003:
            win.blit(question_images_level2[3], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc4 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc4 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc4= False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc4 = False
                    question_points += 1

            if can_qc4 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3004
                            sound_effect()

        if menu == 3004:
            win.blit(question_images_level2[4], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc5 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc5 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc5 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc5 = False

            if can_qc5 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3005
                            sound_effect()

        if menu == 3005:
            win.blit(question_images_level2[5], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc6 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc6= False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc6 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc6 = False

            if can_qc6 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3006
                            sound_effect()

        if menu == 3006:
            win.blit(question_images_level2[6], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc7 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc7 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc7 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc7 = False
                    question_points += 1
            if can_qc7 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3007
                            sound_effect()

        if menu == 3007:
            win.blit(question_images_level2[7], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc8 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc8 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc8 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc8 = False

            if can_qc8 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3008
                            sound_effect()

        if menu == 3008:
            win.blit(question_images_level2[8], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qc9 = False
                    menu = 98 
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qc9 = False
                    menu = 98
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qc9 = False
                    menu = 98
                    question_points += 1
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qc9 = False
                    menu = 98

            if can_qc9 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 3009
                            sound_effect()
        
# level 3 questions
        if menu == 4000:
                win.blit(question_images_level3[0], (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()         
                        can_qcm1 = False
                        question_points += 1
                    if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()             
                        can_qcm1 = False
                    if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()
                        can_qcm1 = False
                    if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()
                        can_qcm1 = False

                if can_qcm1 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4001
                            sound_effect()
                    
        if menu == 4001:
            win.blit(question_images_level3[1], (0, 0))
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm2 = False
                    question_points += 1
                
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm2 = False

            if can_qcm2 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4002
                            sound_effect()
                    
        if menu == 4002:
            win.blit(question_images_level3[2], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm3 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm3 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm3 = False
                    question_points += 1

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm3 = False

            if can_qcm3 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4003
                            sound_effect()
            
        if menu == 4003:
            win.blit(question_images_level3[3], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm4 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm4 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm4= False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm4 = False

            if can_qcm4 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4004
                            sound_effect()

        if menu == 4004:
            win.blit(question_images_level3[4], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm5 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm5 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm5 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm5 = False

            if can_qcm5 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4005
                            sound_effect()

        if menu == 4005:
            win.blit(question_images_level3[5], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm6 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm6= False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm6 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm6 = False
                    question_points += 1

            if can_qcm6 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4006
                            sound_effect()

        if menu == 4006:
            win.blit(question_images_level3[6], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm7 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm7 = False
                    question_points += 1
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm7 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm7 = False
            if can_qcm7 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4007
                            sound_effect()

        if menu == 4007:
            win.blit(question_images_level3[7], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcm8 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcm8 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcm8 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcm8 = False

            if can_qcm8 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 4008
                            sound_effect()

        if menu == 4008:
            win.blit(question_images_level3[8], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    menu = 99
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()      
                    menu = 99
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()           
                    menu = 99
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    question_points += 1
                    sound_effect()
                    menu = 99

# level 4 questions
        if menu == 5000:
                win.blit(question_images_level4[0], (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()         
                        can_qcd1 = False
                        question_points += 1
                    if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()             
                        can_qcd1 = False
                    if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                        sound_effect()
                        can_qcd1 = False
                    if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                        sound_effect()
                        can_qcd1 = False

                if can_qcd1 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5001
                            sound_effect()
                    
        if menu == 5001:
            win.blit(question_images_level4[1], (0, 0))
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd2 = False
                
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd2 = False 
                    
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd2 = False 
                    question_points += 1
                    
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd2 = False

            if can_qcd2 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5002
                            sound_effect()
                    
        if menu == 5002:
            win.blit(question_images_level4[2], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd3 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd3 = False

                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd3 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd3 = False
                    question_points += 1

            if can_qcd3 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5003
                            sound_effect()
            
        if menu == 5003:
            win.blit(question_images_level4[3], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd4 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd4 = False
                    question_points += 1
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd4= False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd4 = False

            if can_qcd4 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5004
                            sound_effect()

        if menu == 5004:
            win.blit(question_images_level4[4], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd5 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd5 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd5 = False
                    question_points += 1

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd5 = False

            if can_qcd5 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5005
                            sound_effect()

        if menu == 5005:
            win.blit(question_images_level4[5], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd6 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd6= False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd6 = False
                    question_points += 1

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd6 = False

            if can_qcd6 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5006
                            sound_effect()

        if menu == 5006:
            win.blit(question_images_level4[6], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd7 = False
                    question_points += 1

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd7 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd7 = False

                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd7 = False

            if can_qcd7 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5007
                            sound_effect()

        if menu == 5007:
            win.blit(question_images_level4[7], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    can_qcd8 = False

                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()  
                    can_qcd8 = False
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    sound_effect()
                    can_qcd8 = False
                    question_points += 1
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    can_qcd8 = False

            if can_qcd8 == False:
                    win.blit(transform_right_arrow, (0, 0))
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 <= mouse_pos[0] <= 100 and 0 <= mouse_pos[1] <= 70:
                            menu = 5008
                            sound_effect()

        if menu == 5008:
            win.blit(question_images_level4[8], (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    menu = 100
                if 200 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()      
                    menu = 100
                if 570 <= mouse_pos[0] <= 880 and 250 <= mouse_pos[1] <= 300:
                    question_points += 1
                    sound_effect()           
                    menu = 100
                if 570 <= mouse_pos[0] <= 880 and 450 <= mouse_pos[1] <= 500:
                    sound_effect()
                    menu = 100

            
        
        if menu == 97:
            win.blit(transform_first_game_map, (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 900 <= mouse_pos[0] <= 1000 and 290 <= mouse_pos[1] <= 390:
                    sound_effect() 
                    menu = 3
        
        if menu == 98:
            win.blit(transform_first_game_map_level2, (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 100 <= mouse_pos[0] <= 200 and 300 <= mouse_pos[1] <= 390:
                    sound_effect() 
                    menu = 4

        if menu == 99:
            win.blit(transform_first_game_map_level3, (0, 0))
            if event.type == MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 455 <= mouse_pos[0] <= 555 and 250 <= mouse_pos[1] <= 300:
                    sound_effect() 
                    menu = 5
        
        if menu == 100:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 950 <= mouse_pos[0] <= 1050 and 130 <= mouse_pos[1] <= 200:
                    sound_effect()
                    menu = 101
        
        if menu == 101:  
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                    sound_effect()
                    menu = 102
        
        if menu == 102:
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 950 <= mouse_pos[0] <= 1050 and 330 <= mouse_pos[1] <= 400:
                    sound_effect()
                    menu = 103
        
        if menu == 103:
            if question_points <= 9:
                ending_1()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                        sound_effect()
                        menu = 104
            if question_points <= 18 and question_points >= 10:
                ending_2() 
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                        sound_effect()
                        menu = 104        
            if question_points <= 36 and question_points >= 19:
                ending_3()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 950 <= mouse_pos[0] <= 1050 and 230 <= mouse_pos[1] <= 300:
                        sound_effect()
                        menu = 104
        
        if menu == 104:
            win.blit(trans_finish, (0, 0))
            f1 = font.render(f"{str(question_points)} / 36", True, black)
            win.blit(f1, (370, 410))
            if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 465 <= mouse_pos[0] <= 585 and 360 <= mouse_pos[1] <= 500:
                        sound_effect()
                        webbrowser.open(r"https://s6.uupload.ir/files/پاسخنامه_5lvp.png")

                

                    
        
       

        
          


    # info
    if menu == -2:
        info1()
    if menu == -3:
        info2()
    if menu == -4:
        info3()
    if menu == -5:
        info4()
    if menu == -6:
        info5()
    if menu == -7:
        info6()

    # sett
    if menu == -1:
        setting()
        
    if menu == 0:
        main_menu()

    if menu == 1:
        first_entering_to_game()

    if menu == 2:
        level_one()
        win.blit(overlay, (0, 0))
        player()
        kamandar()
        if dialog_start_time is None:
            dialog_start_time = time.time()
    # نمایش دیالوگ فعلی
        win.blit(dialog_images[dialog_index], (10, 225))

    # چک کن ۵ ثانیه گذشته
        if time.time() - dialog_start_time >= 4:
            dialog_index += 1
            dialog_start_time = time.time()

        # اگه آخر لیست رسیدیم دیگه ثابت بمونه (یا میتونی ریست کنی)
        if dialog_index >= len(dialog_images):
            dialog_index = len(dialog_images) - 1

        if dialog_index == 11:
            menu = 2000

        # maps view:
    
    if menu == 3:
        level_two()
        win.blit(overlay, (0, 0))
        player()
        prince()
        if dialog_start_time_level2 is None:
            dialog_start_time_level2 = time.time()
    # نمایش دیالوگ فعلی
        win.blit(dialog_images_level2[dialog_index_level2], (10, 225))

    # چک کن ۵ ثانیه گذشته
        if time.time() - dialog_start_time_level2 >= 4:
            dialog_index_level2 += 1
            dialog_start_time_level2 = time.time()

        # اگه آخر لیست رسیدیم دیگه ثابت بمونه (یا میتونی ریست کنی)
        if dialog_index_level2 >= len(dialog_images_level2):
            dialog_index_level2 = len(dialog_images_level2) - 1

        if dialog_index_level2 == 9:
            menu = 3000
    
    if menu == 4:
        win.blit(transform_level3_back_image, (0, 0))
        player()
        minister()
        if dialog_start_time_level3 is None:
            dialog_start_time_level3 = time.time()
    # نمایش دیالوگ فعلی
        win.blit(dialog_images_level3[dialog_index_level3], (10, 225))

    # چک کن ۵ ثانیه گذشته
        if time.time() - dialog_start_time_level3 >= 4:
            dialog_index_level3 += 1
            dialog_start_time_level3 = time.time()

        # اگه آخر لیست رسیدیم دیگه ثابت بمونه (یا میتونی ریست کنی)
        if dialog_index_level3 >= len(dialog_images_level3):
            dialog_index_level3 = len(dialog_images_level3) - 1

        if dialog_index_level3 == 13:
            menu = 4000

    if menu == 5:
        level_four()
        win.blit(overlay, (0, 0))
        player()
        king()
        if dialog_start_time_leve4 is None:
            dialog_start_time_leve4 = time.time()
    # نمایش دیالوگ فعلی
        win.blit(dialog_images_level4[dialog_index_level4], (10, 225))

    # چک کن ۵ ثانیه گذشته
        if time.time() - dialog_start_time_leve4 >= 4:
            dialog_index_level4 += 1
            dialog_start_time_leve4 = time.time()

        # اگه آخر لیست رسیدیم دیگه ثابت بمونه (یا میتونی ریست کنی)
        if dialog_index_level4 >= len(dialog_images_level4):
            dialog_index_level4 = len(dialog_images_level4) - 1

        if dialog_index_level4 == 11:
            menu = 5000



    if menu == 100:
        last()
    if menu == 101:
        last2()
    if menu == 102:
        last3()
            
    # home icon ----> everywhere != 0
    if menu != 0:
        win.blit(transform_home_icon, (980, 5))




    # Update the display
    pygame.display.update()
    clock.tick(fps)

