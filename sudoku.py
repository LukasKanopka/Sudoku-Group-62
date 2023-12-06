import pygame, sys
import sudoku_generator
import copy

# Constants for size and colors
WIDTH, HEIGHT = 450, 450
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)
FONT_COLOR = BLACK
SELECTED_CELL_COLOR = RED

# Code is inspired by Tic tac toe video provided
def draw_game_start(screen):
    # Title fonts and color background
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 30)
    screen.fill(WHITE)

    # Initialize and draw title
    title_surface = start_title_font.render("Select Mode:", 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2 + 65, HEIGHT // 2))
    screen.blit(title_surface, title_rectangle)

    # Initialize text for buttons
    easy_text = button_font.render("Easy", 0, WHITE)
    medium_text = button_font.render("Medium", 0, WHITE)
    hard_text = button_font.render("Hard", 0, WHITE)

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BLACK)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BLACK)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BLACK)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 75, HEIGHT // 2 + 200))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2 + 75, HEIGHT // 2 + 200))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 225, HEIGHT // 2 + 200))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # While loop for main page
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 1
                elif medium_rectangle.collidepoint(event.pos):
                    return 2
                elif hard_rectangle.collidepoint(event.pos):
                    return 3
        pygame.display.update()

def draw_game_screen(board):
    # Draw the grid
    for i in range(GRID_SIZE + 1):
        if (i % 3) == 0:
            # Draw bold lines
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        else:
            # Draw regular lines
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 1)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 1)

    # draw the numbers on the grid
    font = pygame.font.Font(None, 36)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = j * CELL_SIZE + CELL_SIZE // 2
            y = i * CELL_SIZE + CELL_SIZE // 2

            editable = (i, j) not in filled_cells
            selected = selected_cell == (i, j)
            value = str(board[i][j]) if board[i][j] != 0 else ""

            # Differentiate between locked numbers and user entered
            if editable:
                color = GREY if selected else BLACK
            else:
                color = BLUE

            number = font.render(value, True, color)
            x -= number.get_width() // 2
            y -= number.get_height() // 2
            screen.blit(number, (x, y))

def draw_buttons():
    # Make the buttons
    button_font = pygame.font.Font(None, 30)

    reset_text = button_font.render("Reset", 0, WHITE)
    restart_text = button_font.render("Restart", 0, WHITE)
    exit_text = button_font.render("Exit", 0, WHITE)

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(BLACK)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 75, HEIGHT // 2 + 275))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 + 75, HEIGHT // 2 + 275))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 225, HEIGHT // 2 + 275))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

# Track selected cell and state of each cell
selected_cell = None
editable_states = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

# draws the rectangle for the selected cell in red
def draw_selected_cell():
    if selected_cell is not None:
        row, col = selected_cell
        pygame.draw.rect(screen, SELECTED_CELL_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

# updates the values of the board when given a number in the cell
def handle_input_event(event):
    global selected_cell
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // CELL_SIZE
        row = mouse_pos[1] // CELL_SIZE
        selected_cell = (row, col)
    elif event.type == pygame.KEYDOWN and selected_cell is not None:
        row, col = selected_cell
        if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
            value = int(event.unicode)
            if (row, col) not in filled_cells:  # Check if the cell is editable
                board[row][col] = value
                editable_states[row][col] = True  # Set state to editable
        elif event.key == pygame.K_RETURN:
            selected_cell = None
#iterates through each number in the board to make sure that they are equal. If they all are then return true.
def check_game_won(board, solved_board):
    return all(all(cell == solved_board[i][j] for j, cell in enumerate(row)) for i, row in enumerate(board))
  
# draws the game over screen over the sudoku board
def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 100)
    game_over_text = game_over_font.render("Game Over :(", 0, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    restart_button_font = pygame.font.Font(None, 30)
    restart_text = restart_button_font.render("Restart", 0, WHITE)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (10, 10))
    restart_rect = restart_surface.get_rect(center=(WIDTH // 2 - 75, HEIGHT // 2 + 200))

    exit_button_font = pygame.font.Font(None, 30)
    exit_text = exit_button_font.render("Exit", 0, WHITE)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (10, 10))
    exit_rect = exit_surface.get_rect(center=(WIDTH // 2 + 75, HEIGHT // 2 + 200))

    screen.fill(WHITE)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(restart_surface, restart_rect)
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return True
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

# Main body of the game that is run
if __name__ == "__main__":
    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    while True:
        # User chooses easy, med, or hard, empty cells entered accordingly
        user_choice = draw_game_start(screen)
        screen.fill(WHITE)

        if user_choice == 1:
            solved_board, board = sudoku_generator.generate_sudoku(9, 30)
        elif user_choice == 2:
            solved_board, board = sudoku_generator.generate_sudoku(9, 40)
        elif user_choice == 3:
            solved_board, board = sudoku_generator.generate_sudoku(9, 50)

        reset_board = copy.deepcopy(board)

        # Make the buttons
        button_font = pygame.font.Font(None, 30)
        reset_text = button_font.render("Reset", 0, WHITE)
        restart_text = button_font.render("Restart", 0, WHITE)
        exit_text = button_font.render("Exit", 0, WHITE)

        # Initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(BLACK)
        reset_surface.blit(reset_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(BLACK)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(BLACK)
        exit_surface.blit(exit_text, (10, 10))

        # Initialize button rectangle
        reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 75, HEIGHT // 2 + 275))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 + 75, HEIGHT // 2 + 275))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 225, HEIGHT // 2 + 275))

        # Draw buttons
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        # Create a set of filled cells for later reference
        filled_cells = {(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] != 0}

        while True:
            # event loop
            exit_num = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Mouse clicks on reset, restart, exit buttons
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rectangle.collidepoint(event.pos):
                        exit_num = 2
                        break
                    if restart_rectangle.collidepoint(event.pos):
                        exit_num = 1
                        break
                    if exit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                # Movement with arrow keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        row, col = selected_cell
                        selected_cell = (row, col - 1)
                    if event.key == pygame.K_RIGHT:
                        row, col = selected_cell
                        selected_cell = (row, col + 1)
                    if event.key == pygame.K_UP:
                        row, col = selected_cell
                        selected_cell = (row - 1, col)
                    if event.key == pygame.K_DOWN:
                        row, col = selected_cell
                        selected_cell = (row + 1, col)
                handle_input_event(event)

            # Dealing with reset and restart
            if exit_num == 1:
              break
            elif exit_num == 2:
                board = copy.deepcopy(reset_board)

            # Updating screen
            screen.fill(WHITE)
            draw_game_screen(board)
            draw_buttons()
            draw_selected_cell()

            # checks if you won or lost only if board is full
            if all(all(cell != 0 for cell in row) for row in board):
                if check_game_won(board, solved_board):
                    # Game Won
                    game_won_font = pygame.font.Font(None, 100)
                    game_won_text = game_won_font.render("Game Won!", 0, BLACK)
                    game_won_rect = game_won_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

                    exit_button_font = pygame.font.Font(None, 30)
                    exit_text = exit_button_font.render("Exit", 0, WHITE)
                    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
                    exit_surface.fill(BLACK)
                    exit_surface.blit(exit_text, (10, 10))
                    exit_rect = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

                    screen.fill(WHITE)
                    screen.blit(game_won_text, game_won_rect)
                    screen.blit(exit_surface, exit_rect)

                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if exit_rect.collidepoint(event.pos):
                                    pygame.quit()
                                    sys.exit()
                        pygame.display.update()
                else:
                    # Game Over
                    if draw_game_over(screen):
                        # Restart the game
                        screen.fill(WHITE)
                        if user_choice == 1:
                            solved_board, board = sudoku_generator.generate_sudoku(9, 30)
                        elif user_choice == 2:
                            solved_board, board = sudoku_generator.generate_sudoku(9, 40)
                        elif user_choice == 3:
                            solved_board, board = sudoku_generator.generate_sudoku(9, 50)
                        filled_cells = {(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] != 0}

            pygame.display.update()
          
