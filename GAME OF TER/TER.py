import random
import time
sounds.readygo.play()
music.play('bgm')
WIDTH = 1000
HEIGHT = 400
speed_1 = 1
speed_2 = 2
laser_ready = 1
bigbang_ready = 1

hero = Actor('hero_live')
badguy_1 = Actor('czt_live')
badguy_2 = Actor('wzw_live')
badguy_3 = Actor('xyf_live')
badguy_4 = Actor('cll_live')
badguy_5 = Actor('whx_live')
badguy_6 = Actor('lst_live')
bullet = Actor('bullet')
bullet_long = Actor('bullet_long')
bullet_big = Actor('bullet_big')
game_over = Actor('gameover')
game_win = Actor('gamewin')
show_level_2 = Actor('level_2')
show_level_3 = Actor('level_3')
show_level_4 = Actor('level_4')
show_level_5 = Actor('level_5')
show_level_6 = Actor('level_6')
show_level_7 = Actor('level_7')
show_level_8 = Actor('level_8')
show_level_9 = Actor('level_9')
show_level_10 = Actor('level_10')

hero.pos = 400, 200
badguy_1.pos = 1200, 50
badguy_2.pos = 1400, 150
badguy_3.pos = 1500, 200
badguy_4.pos = 1400, 250
badguy_5.pos = 1300, 300
badguy_6.pos = 1500, 50
bullet.pos = 900, 900
bullet_long.pos = 900, 900
bullet_big.pos = 5000, 5000
game_over.pos = 5000, 5000
game_win.pos = 5000, 5000
show_level_2.pos = 5000, 5000
show_level_3.pos = 5000, 5000
show_level_4.pos = 5000, 5000
show_level_5.pos = 5000, 5000
show_level_6.pos = 5000, 5000
show_level_7.pos = 5000, 5000
show_level_8.pos = 5000, 5000
show_level_9.pos = 5000, 5000
show_level_10.pos = 5000, 5000

hero.score = 0
hero.level = 1
hero.life = 100

def draw():
    screen.clear()
    screen.fill((0, 0, 128))
    screen.blit('background', (0, 0))
    screen.blit('girls', (0, 0))
    screen.blit('like', (20, -15))
    screen.blit('like_2', (15, 330))
    screen.blit('like_3', (45, 95))
    hero.draw()
    badguy_1.draw()
    badguy_2.draw()
    badguy_3.draw()
    badguy_4.draw()
    badguy_5.draw()
    badguy_6.draw()
    bullet.draw()
    bullet_long.draw()
    bullet_big.draw()
    game_over.draw()
    game_win.draw()
    show_level_2.draw()
    show_level_3.draw()
    show_level_4.draw()
    show_level_5.draw()
    show_level_6.draw()
    show_level_7.draw()
    show_level_8.draw()
    show_level_9.draw()
    show_level_10.draw()

    if laser_ready == 1:
        screen.draw.text(
        "------------------- Sir ! Laser gun is ready ! ! !",
        (100, 375),
        color="yellow",
        fontsize=30,shadow=(1, 1)
        )
    else:
        screen.draw.text(
        "------------------- Laser gun is preparing",
        (100, 375),
        color="red",
        fontsize=30,shadow=(1, 1)
        )

    if bigbang_ready == 1:
        screen.draw.text(
        "--------------------- Sir ! Big Bang is ready ! ! !",
        (550, 375),
        color="yellow",
        fontsize=30,shadow=(1, 1)
        )
    else:
        screen.draw.text(
        "--------------------- Big Bang is preparing",
        (550, 375),
        color="red",
        fontsize=30,shadow=(1, 1)
        )

    screen.draw.text(
        'Level : '+str(hero.level),
        color='yellow',
        midtop=(WIDTH-600, 8),
        fontsize=40,
        shadow=(1, 1)
    )

    screen.draw.text(
        'Win in 600  =====>>',
        color='white',
        midtop=(WIDTH-300, 15),
        fontsize=35,
        shadow=(1, 1)
    )

    screen.draw.text(
        'Life : '+str(hero.life),
        color='yellow',
        midtop=(WIDTH-800, 8),
        fontsize=40,
        shadow=(1, 1)
    )

    screen.draw.text(
        'Score:'+str(hero.score),
        color='yellow',
        midtop=(WIDTH-110, 10),
        fontsize=50,
        shadow=(1, 1)
    )

def set_show_level_normal():
    show_level_2.pos = 2000, 2000
    show_level_3.pos = 2000, 2000
    show_level_4.pos = 2000, 2000
    show_level_5.pos = 2000, 2000
    show_level_6.pos = 2000, 2000
    show_level_7.pos = 2000, 2000
    show_level_8.pos = 2000, 2000
    show_level_9.pos = 2000, 2000
    show_level_10.pos = 2000, 2000

def win_game():
    music.play('win')
    time.sleep(1000)

def end_game():
    music.play('gameover')
    time.sleep(1000)

def add_score():
    hero.score += 1
    update_level()

def set_hero_normal():
    hero.image = 'hero_live'

def set_badguy_1_normal():
    badguy_1.image = 'czt_live'
    badguy_1.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_badguy_2_normal():
    badguy_2.image = 'wzw_live'
    badguy_2.pos = WIDTH + 200, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_badguy_3_normal():
    badguy_3.image = 'xyf_live'
    badguy_3.pos = WIDTH + 100, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_badguy_4_normal():
    badguy_4.image = 'cll_live'
    badguy_4.pos = WIDTH + 100, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_badguy_5_normal():
    badguy_5.image = 'whx_live'
    badguy_5.pos = WIDTH + 300, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_badguy_6_normal():
    badguy_6.image = 'lst_live'
    badguy_6.pos = WIDTH + 300, random.randint(50, HEIGHT-50)
    if hero.life <= 0:
        game_over.pos = 500, 200
        clock.schedule_unique(end_game, 0.5)

def set_bullet_normal():
    bullet.pos = 0, 800

def set_bullet_long_normal():
    bullet_long.pos = 5000, 5000

def set_bullet_big_normal():
    bullet_big.pos == 5000, 5000

def update_level():
    global speed_1
    global speed_2
    if hero.score == 50:
        hero.score = 51
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up.play()
        show_level_2.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 100:
        hero.score = 101
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up_2.play()
        show_level_3.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 150:
        hero.score = 151
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up.play()
        show_level_4.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 200:
        hero.score = 201
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up_3.play()
        show_level_5.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 350:
        hero.score = 351
        speed_1 += 1
        speed_2 += 1
        sounds.level_up.play()
        show_level_6.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 400:
        hero.score = 401
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up_2.play()
        show_level_7.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 450:
        hero.score = 451
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up.play()
        show_level_8.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 500:
        hero.score = 501
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up_3.play()
        show_level_9.pos = 500, 100
        clock.schedule_unique(set_show_level_normal, 2.5)
    if hero.score == 550:
        hero.score = 551
        speed_1 += 1
        speed_2 += 1
        hero.level += 1
        sounds.level_up.play()
        clock.schedule_unique(set_show_level_normal, 2.5)
        show_level_10.pos = 500, 100
    if hero.score > 600:
        game_win.pos = 500, 200
        music.stop()
        clock.schedule_unique(win_game, 0.5)

def update_badguys():
    badguy_1.right -= speed_2
    if badguy_1.right < 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_1_normal()
    badguy_2.right -= speed_1
    if badguy_2.right == 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_2_normal()
    badguy_3.right -= speed_2
    if badguy_3.right < 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_3_normal()
    badguy_4.right -= speed_1
    if badguy_4.right < 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_4_normal()
    badguy_5.right -= speed_2
    if badguy_5.right < 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_5_normal()
    badguy_6.right -= speed_1
    if badguy_6.right < 0:
        hero.life -= 1
        sounds.hurt.play()
        set_badguy_6_normal()

def update():
    update_badguys()
    bullet.right += 70
    bullet_big.right += 6

    if bullet_big.right > 2000:
        set_bullet_big_normal()

    if bullet_long.top > badguy_1.top:
        if bullet_long.top < badguy_1.top + 90:
            sounds.boom.play()
            badguy_1.image = 'czt_die'
            set_badguy_1_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)
    if bullet_long.top > badguy_2.top:
        if bullet_long.top < badguy_2.top + 90:
            sounds.boom.play()
            badguy_2.image = 'wzw_die'
            set_badguy_2_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)
    if bullet_long.top > badguy_3.top:
        if bullet_long.top < badguy_3.top + 90:
            sounds.boom.play()
            badguy_3.image = 'xyf_die'
            set_badguy_3_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)
    if bullet_long.top > badguy_4.top:
        if bullet_long.top < badguy_4.top + 90:
            sounds.boom.play()
            badguy_4.image = 'cll_die'
            set_badguy_4_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)
    if bullet_long.top > badguy_5.top:
        if bullet_long.top < badguy_5.top + 90:
            sounds.boom.play()
            badguy_5.image = 'whx_die'
            set_badguy_5_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)
    if bullet_long.top > badguy_6.top:
        if bullet_long.top < badguy_6.top + 90:
            sounds.boom.play()
            badguy_6.image = 'lst_die'
            set_badguy_6_normal()
            clock.schedule_unique(add_score, 0.1)
            clock.schedule_unique(set_bullet_long_normal, 0.5)

    if bullet_big.collidepoint(badguy_1.pos):
        sounds.die.play()
        badguy_1.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_1.image = 'czt_live'
    if bullet_big.collidepoint(badguy_2.pos):
        sounds.boom.play()
        badguy_2.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_2.image = 'wzw_live'
    if bullet_big.collidepoint(badguy_3.pos):
        sounds.die.play()
        badguy_3.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_3.image = 'xyf_live'
    if bullet_big.collidepoint(badguy_4.pos):
        sounds.boom.play()
        badguy_4.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_4.image = 'cll_live'
    if bullet_big.collidepoint(badguy_5.pos):
        sounds.boom.play()
        badguy_5.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_5.image = 'whx_live'
    if bullet_big.collidepoint(badguy_6.pos):
        sounds.boom.play()
        badguy_6.pos = WIDTH + 150, random.randint(50, HEIGHT-50)
        badguy_6.image = 'lst_live'

    if bullet.collidepoint(badguy_1.pos):
        badguy_1.image = 'czt_die'
        sounds.die_2.play()
        set_bullet_normal()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_1_normal, 0.2)
    if bullet.collidepoint(badguy_2.pos):
        badguy_2.image = 'wzw_die'
        set_bullet_normal()
        sounds.die_3.play()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_2_normal, 0.2)
    if bullet.collidepoint(badguy_3.pos):
        badguy_3.image = 'xyf_die'
        sounds.die.play()
        set_bullet_normal()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_3_normal, 0.2)
    if bullet.collidepoint(badguy_4.pos):
        badguy_4.image = 'cll_die'
        sounds.die_4.play()
        set_bullet_normal()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_4_normal, 0.2)
    if bullet.collidepoint(badguy_5.pos):
        badguy_5.image = 'whx_die'
        sounds.die_2.play()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_5_normal, 0.2)
        update_level()
    if bullet.collidepoint(badguy_6.pos):
        badguy_6.image = 'lst_die'
        sounds.die_4.play()
        clock.schedule_unique(add_score, 0.3)
        clock.schedule_unique(set_badguy_6_normal, 0.2)
        update_level()

    if hero.collidepoint(badguy_1.pos):
        badguy_1.image = 'czt_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.4)
        sounds.eat.play()
        set_badguy_1_normal()
        clock.schedule_unique(add_score, 0.2)
    if hero.collidepoint(badguy_2.pos):
        badguy_2.image = 'wzw_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.4)
        sounds.eat.play()
        set_badguy_2_normal()
        clock.schedule_unique(add_score, 0.2)
    if hero.collidepoint(badguy_3.pos):
        badguy_3.image = 'xyf_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.4)
        sounds.eat.play()
        set_badguy_3_normal()
        clock.schedule_unique(add_score, 0.2)
    if hero.collidepoint(badguy_4.pos):
        badguy_4.image = 'cll_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.4)
        sounds.eat.play()
        set_badguy_4_normal()
        clock.schedule_unique(add_score, 0.2)
    if hero.collidepoint(badguy_5.pos):
        badguy_5.image = 'whx_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.04)
        sounds.eat.play()
        set_badguy_5_normal()
        clock.schedule_unique(add_score, 0.2)
    if hero.collidepoint(badguy_6.pos):
        badguy_6.image = 'lst_die'
        hero.image = 'hero_eat'
        clock.schedule_unique(set_hero_normal, 0.04)
        sounds.eat.play()
        set_badguy_6_normal()
        clock.schedule_unique(add_score, 0.2)

def set_laser_ready():
    global laser_ready
    laser_ready = 1

def set_bigbang_ready():
    global bigbang_ready
    bigbang_ready = 1

def on_mouse_down(pos):
    hero.pos = pos

def bullet_laser_shoot():
    global laser_ready
    laser_ready = 0
    clock.schedule_unique(set_laser_ready, 4)
    bullet_long.pos = hero.pos
    sounds.laser.play()
    hero.image = 'hero_shoot'
    clock.schedule_unique(set_hero_normal, 0.5)
    clock.schedule_unique(set_bullet_long_normal, 0.5)

def bullet_bigbang_shoot():
    global bigbang_ready
    bigbang_ready = 0
    clock.schedule_unique(set_bigbang_ready, 8)
    bullet_big.pos = 0, 200
    sounds.warning.play()
    hero.image = 'hero_big'
    clock.schedule_unique(set_hero_normal, 3.5)

def on_key_down(key):
    if key == keys.J:
        bullet.pos = hero.pos
        sounds.shoot.play()
    elif key == key.L:
        if laser_ready == 1:
            bullet_laser_shoot()
    elif key == keys.I:
        if bigbang_ready == 1:
            bullet_bigbang_shoot()
    elif key == key.W:
        hero.top -= 60
        if hero.top < 0:
            hero.top = 0
    elif key == key.S:
        hero.top += 60
        if hero.top > HEIGHT - 100:
            hero.top = HEIGHT - 100
    elif key == key.A:
        hero.left -= 50
        if hero.left < 0:
            hero.left = 0
    elif key == key.D:
        hero.left += 50
        if hero.left > WIDTH - hero.width:
            hero.left = WIDTH - hero.width