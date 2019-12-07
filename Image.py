import pygame

# 스프라이트 클래스 정의
class SimpleSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):  # 생성자 파라미터로 스프라이트에 사용될 이미지 경로와 스프라이트 초기 위치를 받는다
        pygame.sprite.Sprite.__init__(self)
        self.user_src_image = pygame.image.load(image)  # 스프라이트에 사용될 이미지를 저장할 사용자 변수
        self.user_position = position  # 스프라이트의 위치를 저장할 사용자 변수
        self.user_rotation = 30  # 스프라이트의 회전 각도를 저장할 사용자 변수

    def update(self):  # 스프라이트의 상태를 업데이트 하는 함수. 필요에 따라 파라미터가 추가될 수도 있다.

        # 여기에 게임 상태에 따라 스프라이트의 위치(user_position), 회전 각도(user_rotation), 이미지(user_src_image)를 변경시키는 코드가 들어가야 한다.
        # {{
        # ...
        # }}

        # 출력에 사용될 이미지, 위치를 정한다
        self.image = pygame.transform.rotate(self.user_src_image, self.user_rotation)  # 이미지를 회전 각도 만큼 회전시킨다
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position  # 이미지의 출력 위치를 정한다



# 초기화시 해야할 부분
multiple = [
    SimpleSprite('simple.png', (100, 100)),
    SimpleSprite('simple.png', (100, 200)),
    SimpleSprite('simple.png', (100, 300))
]
multiple_group = pygame.sprite.RenderPlain(*multiple)  # 그룹으로 사용시 * 연산자가 들어가야 한다

# -> RenderPlain 클래스는 여러개의 스프라이트를 묶어주는 역활을 하며,
# 상태 업데이트나 화면에 그릴 때에 RenderPlain 클래스를 통해서 하게된다.

...

# 게임 상태 업데이트시 해야할 부분
multiple_group.update()  # RenderPlain 객체를 통해 업데이트한다

...

# 게임 상태 화면에 출력시 해야할 부분
multiple_group.draw(screen)  # RenderPlain 객체를 통해 출력한다

