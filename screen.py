import pygame 
from pygame.locals import *
from main import *
from grafics import plot_fit_mean
import pylab
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

def plot_graph(data, size, pos, title=''):
    matplotlib.use("Agg")
    fig = pylab.figure(figsize=[size[0]//100, size[1]//100], dpi=100,)
    ax = fig.gca()

    plt.style.use('ggplot')
    ax.plot(data[0], color='green')
    ax.plot(data[1])

    plt.title(title, fontsize=13, fontweight='bold')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, pos)

def write(text, pos, size=32):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surface = font.render(text, True, (0, 0, 0), (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = pos

    screen.blit(text_surface, text_rect)

def draw_pts(pts):
    for pt in pts:
        pygame.draw.circle(screen, (255, 0, 0), (pt[0]+400, pt[1]), 5)
        pygame.draw.circle(screen, (0, 0, 0), (pt[0]+400, pt[1]), 5, 2)

def draw_links(pts, matrix):
    color = 'BLUE'
    for i in range(len(matrix)-1):
        pygame.draw.line(screen, color, (pts[matrix[i]][0]+400, pts[matrix[i]][1]), (pts[matrix[i-1]][0]+400, pts[matrix[i-1]][1]), 3)
    pygame.draw.line(screen, color, (pts[matrix[-2]][0]+400, pts[matrix[-2]][1]), (pts[matrix[-1]][0]+400, pts[matrix[-1]][1]), 3)

def draw_subt():
    x, y = 400, 600
    pygame.draw.line(screen, (200, 30, 30), (x, y), (x+18, y), 3)
    pygame.draw.line(screen, (30, 170, 30), (x, y+20), (x+18, y+20), 3)

    write('Fitness do melhor indivíduo.', (x+100, y), 12)
    write('Média de fitness da população.', (x+110, y+20), 12)

def write_infos():
    x, y = 190, 150
    size = 22
    write('Geração: ' + str(gen), (x, y), size)
    write('Menor Distância Total : ' + str(int(pop.individuals[0].total_dis))+' km', (x, y+20), size)



pygame.init()

bg_img = pygame.image.load('mapa-capitais.png')
screen_size = (bg_img.get_width()+400, bg_img.get_height())
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Traveling Saleman')


pts = [(237, 54), (406, 97), (250, 155), (119, 283), (183, 259), (322, 375), (346, 462), (435, 395), (460, 380), (456, 281), (458, 130), (531, 158), (553, 195), (624, 177), (678, 214), (683, 236), (682, 252), (668, 278), (644, 301), (622, 332), (575, 464), (524, 455), (530, 506), (476, 517), (433, 549), (400, 628), (441, 586)]
n_points = len(pts)
pop = Population(800, n_points)
mean_fit_list = []
best_fit_list = []

gen = 0
fps = 10
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    screen.fill('WHITE')

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 1
            if event.key == K_DOWN:
                fps -= 1

        if event.type == QUIT:
            pygame.quit()

    screen.blit(bg_img, (400, 0))
    draw_links(pts, pop.individuals[0].genome)
    draw_pts(pts)
    draw_subt()
    write_infos()
    pop.fit_pop(pts)
    mean_fit_list.append(pop.mean_fit)
    best_fit_list.append(pop.individuals[0].fit)

    graph_size = 450, 450
    plot_graph((mean_fit_list, best_fit_list), graph_size, (0 , screen_size[1]-graph_size[1]+50), title='Fitness')

    print('-'*13)
    print(f'gen: {gen}')
    print(f'best fit: {int(pop.mean_fit*10)}')
    print(f'mean fit: {int(pop.individuals[0].fit*10)}')


    gen += 1
    pop.new_population()
    pygame.display.update()

