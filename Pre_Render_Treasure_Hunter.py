import tkinter as tk
import random

class TreasureHuntGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Treasure Hunt")

        self.board_size = 10
        self.cell_size = 50

        # Set the window size and prevent resizing
        self.window_width = self.board_size * self.cell_size
        self.window_height = self.board_size * self.cell_size + 100
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)

        # Initialize game elements but do not draw them yet
        self.player_x, self.player_y = 0, 0
        self.treas_x, self.treas_y = random.randint(1, self.board_size - 2), random.randint(1, self.board_size - 2)
        self.visited_tiles = {}  # Store visited tiles with their detailed design state
        self.biomes = []

        # Initialize dragon's position and body
        self.dragon_body = []
        self.dragon_coins_collected = 0  # Track dragon's coins

        # Initialize coins and knight's coin counter
        self.coins = []
        self.knight_coins = 0

        # Create the medieval-themed title screen without using images
        self.create_title_screen()

    def create_title_screen(self):
        # Create a frame for the title screen
        self.title_frame = tk.Frame(self.root, bg='black', width=self.window_width, height=self.window_height)
        self.title_frame.pack()

        # Create canvas for the title graphics
        self.title_canvas = tk.Canvas(self.title_frame, width=self.window_width, height=self.window_height, bg='black', highlightthickness=0)
        self.title_canvas.pack()

        # Draw the medieval-themed title without using images
        self.draw_medieval_title()

        # Add the "Start Game" button without the message textbox
        self.start_button = tk.Button(self.title_frame, text="Start Game", font=('Old English Text MT', 20), bg='#DAA520', fg='black', command=self.start_game)
        self.start_button_window = self.title_canvas.create_window(self.window_width // 2, self.window_height // 2 + 200, window=self.start_button)

    def draw_medieval_title(self):
        # Draw a parchment background
        self.title_canvas.create_rectangle(50, 50, self.window_width - 50, self.window_height - 50, fill='#F5DEB3', outline='#8B4513', width=5)

        # Draw the stylized "Treasure Hunt" title in medieval font
        self.title_canvas.create_text(
            self.window_width // 2,
            self.window_height // 2  -150,
            text="Treasure Hunt",
            font=('Old English Text MT', 40, 'bold'),
            fill='#8B0000'
        )

        # Add medieval decorative elements using drawing methods
        # Crossed swords beneath the title
        self.draw_crossed_swords()

        # Shields on either side of the title
        self.draw_shields()

        # Torches on the sides
        self.draw_torches()

    def draw_crossed_swords(self):
        center_x = self.window_width // 2
        center_y = self.window_height // 2

        # Left sword
        self.title_canvas.create_line(
            center_x - 60, center_y + 20,
            center_x, center_y + 80,
            fill='silver', width=4
        )
        self.title_canvas.create_polygon(
            center_x - 60, center_y + 20,
            center_x - 70, center_y + 10,
            center_x - 50, center_y + 10,
            fill='silver', outline='black'
        )
        # Sword hilt
        self.title_canvas.create_rectangle(
            center_x - 5, center_y + 75,
            center_x + 5, center_y + 85,
            fill='#8B4513', outline='black'
        )
        self.title_canvas.create_line(
            center_x - 10, center_y + 80,
            center_x + 10, center_y + 80,
            fill='#8B4513', width=5
        )

        # Right sword
        self.title_canvas.create_line(
            center_x + 60, center_y + 20,
            center_x, center_y + 80,
            fill='silver', width=4
        )
        self.title_canvas.create_polygon(
            center_x + 60, center_y + 20,
            center_x + 70, center_y + 10,
            center_x + 50, center_y + 10,
            fill='silver', outline='black'
        )
        # Sword hilt
        self.title_canvas.create_rectangle(
            center_x - 5, center_y + 75,
            center_x + 5, center_y + 85,
            fill='#8B4513', outline='black'
        )
        self.title_canvas.create_line(
            center_x - 10, center_y + 80,
            center_x + 10, center_y + 80,
            fill='#8B4513', width=5
        )

    def draw_shields(self):
        # Left shield
        self.title_canvas.create_polygon(
            100, self.window_height // 2 - 100,
            130, self.window_height // 2 - 70,
            115, self.window_height // 2 - 40,
            85, self.window_height // 2 - 40,
            70, self.window_height // 2 - 70,
            fill='#8B4513', outline='black', width=2
        )
        # Emblem on the shield
        self.title_canvas.create_oval(
            90, self.window_height // 2 - 80,
            110, self.window_height // 2 - 60,
            fill='red', outline='gold', width=2
        )

        # Right shield
        self.title_canvas.create_polygon(
            self.window_width - 100, self.window_height // 2 - 100,
            self.window_width - 70, self.window_height // 2 - 70,
            self.window_width - 85, self.window_height // 2 - 40,
            self.window_width - 115, self.window_height // 2 - 40,
            self.window_width - 130, self.window_height // 2 - 70,
            fill='#8B4513', outline='black', width=2
        )
        # Emblem on the shield
        self.title_canvas.create_oval(
            self.window_width - 110, self.window_height // 2 - 80,
            self.window_width - 90, self.window_height // 2 - 60,
            fill='red', outline='gold', width=2
        )

    def draw_torches(self):
        # Left torch
        self.title_canvas.create_line(
            80, self.window_height // 2 + 50,
            80, self.window_height // 2 + 100,
            fill='brown', width=6
        )
        self.title_canvas.create_polygon(
            75, self.window_height // 2 + 50,
            85, self.window_height // 2 + 50,
            80, self.window_height // 2 + 30,
            fill='orange', outline='red'
        )

        # Right torch
        self.title_canvas.create_line(
            self.window_width - 80, self.window_height // 2 + 50,
            self.window_width - 80, self.window_height // 2 + 100,
            fill='brown', width=6
        )
        self.title_canvas.create_polygon(
            self.window_width - 85, self.window_height // 2 + 50,
            self.window_width - 75, self.window_height // 2 + 50,
            self.window_width - 80, self.window_height // 2 + 30,
            fill='orange', outline='red'
        )

    def start_game(self):
        # Generate biomes and load assets with loading screen
        self.generate_biomes()
        self.load_assets()

    def load_assets(self):
        # Create a loading screen overlay
        self.loading_overlay = tk.Frame(self.root, bg='black', width=self.window_width, height=self.window_height)
        self.loading_overlay.place(x=0, y=0)

        # Center the loading message and progress bar
        self.loading_label = tk.Label(self.loading_overlay, text="Loading Assets...", font=('Old English Text MT', 30), bg='black', fg='white')
        self.loading_label.place(relx=0.5, rely=0.4, anchor='center')

        # Create a progress bar
        self.progress_bar = tk.Canvas(self.loading_overlay, width=400, height=30, bg='white', highlightthickness=0)
        self.progress_bar.place(relx=0.5, rely=0.5, anchor='center')
        self.progress_rect = self.progress_bar.create_rectangle(2, 2, 0, 28, fill='green', outline='')

        self.root.update()

        # Generate textures for all tiles
        total_tiles = self.board_size * self.board_size
        tile_count = 0

        self.tile_textures = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                # Determine biome for this tile
                biome_type = None
                biome_colors = None
                for biome in self.biomes:
                    if (i, j) in biome['tiles']:
                        biome_type = biome['type']
                        biome_colors = biome['colors']
                        break
                # Generate texture for the tile
                if biome_type is not None:
                    tile_texture = self.generate_tile_texture(biome_colors, biome_type)
                else:
                    # Generate cobblestone texture for walkways
                    cobblestone_colors = ['#7F7F7F', '#8C8C8C', '#999999']
                    tile_texture = self.generate_tile_texture(cobblestone_colors, 'cobblestone', i, j)

                self.tile_textures[i][j] = tile_texture

                # Update progress bar
                tile_count += 1
                progress = (tile_count / total_tiles) * 400  # Progress bar width is 400
                self.progress_bar.coords(self.progress_rect, 2, 2, 2 + progress, 28)
                self.root.update()

        # Loading complete, wait for 1 second
        self.root.after(1000, self.after_loading)

    def after_loading(self):
        # Destroy loading screen
        self.loading_overlay.destroy()

        # Remove the title screen
        self.title_frame.destroy()

        # Create game widgets and draw the game board
        self.create_game_widgets()
        self.draw_board()
        self.draw_player()
        # Don't draw the treasure yet
        # self.draw_treasure()

        # Generate coins and draw them
        self.generate_coins()
        self.draw_coins()

        # Uncover the player's starting tile
        self.canvas.delete(f'cover_{self.player_x}_{self.player_y}')

        # Bind key events
        self.root.bind("<KeyPress>", self.key_pressed)
        self.current_biome = None
        self.previous_biome = None
        self.treasure_message_shown = False
        self.treasure_visible = False  # Treasure is initially hidden

        # Initialize the dragon snake
        self.init_dragon_snake()
        self.draw_dragon_snake()

        # Start the dragon's actions
        self.dragon_action_running = True
        self.dragon_action()

    def generate_tile_texture(self, colors, biome_type, i=None, j=None):
        tile_design = []
        if biome_type == 'cobblestone':
            # Generate brick pattern
            brick_width = 20
            brick_height = 10
            for y in range(0, self.cell_size, brick_height):
                offset = brick_width // 2 if (y // brick_height) % 2 == 1 else 0
                for x in range(-offset, self.cell_size + offset, brick_width):
                    x0 = x + random.randint(-2, 2)
                    y0 = y + random.randint(-1, 1)
                    x1 = x0 + brick_width + random.randint(-4, 0)
                    y1 = y0 + brick_height + random.randint(-2, 0)

                    # Ensure the bricks stay within the tile
                    x0 = max(0, x0)
                    y0 = max(0, y0)
                    x1 = min(self.cell_size, x1)
                    y1 = min(self.cell_size, y1)

                    color = random.choice(colors)
                    tile_design.append(('rectangle', x0, y0, x1, y1, color))

                    # Add cracks
                    if random.random() < 0.5:
                        num_cracks = random.randint(1, 3)
                        for _ in range(num_cracks):
                            crack_x0 = x0 + random.uniform(1, max(1, x1 - x0 - 2))
                            crack_y0 = y0 + random.uniform(1, max(1, y1 - y0 - 2))
                            crack_length = random.uniform(2, 5)
                            crack_x1 = crack_x0 + crack_length * random.uniform(-1, 1)
                            crack_y1 = crack_y0 + crack_length * random.uniform(-1, 1)
                            # Ensure cracks stay within brick boundaries
                            crack_x1 = min(max(crack_x1, x0), x1)
                            crack_y1 = min(max(crack_y1, y0), y1)
                            tile_design.append(('line', crack_x0, crack_y0, crack_x1, crack_y1, '#4d4d4d'))

            # Add dirt borders with irregular edges
            biome_borders = self.get_biome_borders(i, j)
            dirt_colors = ['#654321', '#5C4033', '#4E3524']
            for side in biome_borders:
                color = random.choice(dirt_colors)
                tile_design.append(('dirt_border_irregular', side, color))
        else:
            # Generate texture for other biomes
            pattern_size = 4  # Each detailed block will be 4x4 pixels
            for m in range(0, self.cell_size, pattern_size):
                for n in range(0, self.cell_size, pattern_size):
                    color = random.choice(colors)
                    tile_design.append(('rectangle_simple', m, n, color))
        return (biome_type, tile_design)

    def get_biome_borders(self, i, j):
        borders = []
        directions = {
            'top': (0, -1),
            'bottom': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }
        for side, (dx, dy) in directions.items():
            ni, nj = i + dx, j + dy
            if 0 <= ni < self.board_size and 0 <= nj < self.board_size:
                for biome in self.biomes:
                    if (ni, nj) in biome['tiles']:
                        borders.append(side)
                        break  # No need to check other biomes for this side
        return borders

    def create_game_widgets(self):
        # Create canvas for game board
        self.canvas = tk.Canvas(self.root, width=self.window_width, height=self.window_height - 100, bg='black')
        self.canvas.pack()

        # Create message bar with fixed width
        self.message_frame = tk.Frame(self.root, bg='black', width=self.window_width, height=100)
        self.message_frame.pack_propagate(False)
        self.message_frame.pack()

        # Coin counter label on its own line
        self.coin_frame = tk.Frame(self.message_frame, bg='black', width=self.window_width, height=30)
        self.coin_frame.pack(fill=tk.X)
        self.coin_label = tk.Label(
            self.coin_frame, text=f"Coins Collected: {self.knight_coins}",
            font=('Terminal', 12), bg='black', fg='yellow',
            anchor='w', justify='left'
        )
        self.coin_label.pack(side=tk.LEFT)

        # Message label on its own line
        self.text_frame = tk.Frame(self.message_frame, bg='black', width=self.window_width, height=70)
        self.text_frame.pack(fill=tk.X)
        self.message_label = tk.Label(
            self.text_frame, text="", font=('Terminal', 12), bg='black', fg='white',
            wraplength=self.window_width, anchor='w', justify='left'
        )
        self.message_label.pack(side=tk.LEFT)

    def generate_biomes(self):
        excluded_area = [(i, j) for i in range(self.treas_x - 1, self.treas_x + 2) for j in range(self.treas_y - 1, self.treas_y + 2)]
        all_coordinates = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if (i, j) not in excluded_area]
        random.shuffle(all_coordinates)

        biome_types = ['jungle', 'lake', 'ruins', 'field', 'grove', 'outcrop', 'waterfall']
        biome_colors = {
            'jungle': ['#0a580a', '#1c8e1c', '#4caf50'],
            'lake': ['#1e3f66', '#4682b4', '#5f9ea0'],
            'ruins': ['#555555', '#808080', '#a9a9a9'],
            'field': ['#c2b280', '#e5c967', '#f7d679'],
            'grove': ['#013220', '#006400', '#228b22'],
            'outcrop': ['#654321', '#8b4513', '#a0522d'],
            'waterfall': ['#0073e6', '#00bfff', '#add8e6']
        }

        biome_tiles = []
        used_coordinates = set()

        for biome_type in biome_types:
            if not all_coordinates:
                break

            start_tile = all_coordinates.pop()
            biome_group = [start_tile]
            used_coordinates.add(start_tile)

            while len(biome_group) < 13 and all_coordinates:
                potential_tiles = [(tile[0] + dx, tile[1] + dy) for tile in biome_group for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
                adjacent_tiles = [tile for tile in potential_tiles if tile in all_coordinates and tile not in used_coordinates]
                if not adjacent_tiles:
                    break
                next_tile = random.choice(adjacent_tiles)
                all_coordinates.remove(next_tile)
                used_coordinates.add(next_tile)
                biome_group.append(next_tile)

            biome_tiles.append({'type': biome_type, 'tiles': biome_group, 'colors': biome_colors[biome_type]})

        self.biomes = biome_tiles

    def draw_board(self):
        self.tiles = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                x0, y0 = i * self.cell_size, j * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                tile_texture = self.tile_textures[i][j]
                if tile_texture:
                    biome_type, tile_design = tile_texture
                    # Draw the tile using the stored tile_design
                    for design in tile_design:
                        if isinstance(design, tuple):
                            if design[0] == 'rectangle_simple':
                                _, dx, dy, color = design
                                self.canvas.create_rectangle(
                                    x0 + dx, y0 + dy, x0 + dx + 4, y0 + dy + 4,
                                    outline=color, fill=color, tags=f'tile_{i}_{j}'
                                )
                            elif design[0] == 'rectangle':
                                _, x_start, y_start, x_end, y_end, color = design
                                self.canvas.create_rectangle(
                                    x0 + x_start, y0 + y_start, x0 + x_end, y0 + y_end,
                                    outline='black', fill=color, tags=f'tile_{i}_{j}'
                                )
                            elif design[0] == 'line':
                                _, x_start, y_start, x_end, y_end, color = design
                                self.canvas.create_line(
                                    x0 + x_start, y0 + y_start, x0 + x_end, y0 + y_end,
                                    fill=color, width=1, tags=f'tile_{i}_{j}'
                                )
                            elif design[0] == 'dirt_border_irregular':
                                _, side, color = design
                                self.draw_irregular_dirt_border(x0, y0, x1, y1, side, color, f'tile_{i}_{j}')
                # Cover the tile with a black rectangle to hide it
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='black', tags=f'cover_{i}_{j}')
                row.append((x0, y0, x1, y1))
            self.tiles.append(row)

    def draw_irregular_dirt_border(self, x0, y0, x1, y1, side, color, tag):
        # Generate random points along the edge to create an irregular border
        points = []
        if side == 'top':
            points = [(x0, y0)]
            for i in range(1, 10):
                xi = x0 + i * (x1 - x0) / 10 + random.randint(-2, 2)
                yi = y0 + random.randint(0, 5)
                xi = min(max(x0, xi), x1)
                yi = min(max(y0, yi), y1)
                points.append((xi, yi))
            points.append((x1, y0))
            points.append((x1, y0 + 5))
            points.append((x0, y0 + 5))
        elif side == 'bottom':
            points = [(x0, y1)]
            for i in range(1, 10):
                xi = x0 + i * (x1 - x0) / 10 + random.randint(-2, 2)
                yi = y1 - random.randint(0, 5)
                xi = min(max(x0, xi), x1)
                yi = min(max(y0, yi), y1)
                points.append((xi, yi))
            points.append((x1, y1))
            points.append((x1, y1 - 5))
            points.append((x0, y1 - 5))
        elif side == 'left':
            points = [(x0, y0)]
            for i in range(1, 10):
                xi = x0 + random.randint(0, 5)
                yi = y0 + i * (y1 - y0) / 10 + random.randint(-2, 2)
                xi = min(max(x0, xi), x1)
                yi = min(max(y0, yi), y1)
                points.append((xi, yi))
            points.append((x0, y1))
            points.append((x0 + 5, y1))
            points.append((x0 + 5, y0))
        elif side == 'right':
            points = [(x1, y0)]
            for i in range(1, 10):
                xi = x1 - random.randint(0, 5)
                yi = y0 + i * (y1 - y0) / 10 + random.randint(-2, 2)
                xi = min(max(x0, xi), x1)
                yi = min(max(y0, yi), y1)
                points.append((xi, yi))
            points.append((x1, y1))
            points.append((x1 - 5, y1))
            points.append((x1 - 5, y0))
        # Draw the polygon
        self.canvas.create_polygon(*points, fill=color, outline='', tags=tag)

    def draw_player(self):
        x0, y0 = self.player_x * self.cell_size, self.player_y * self.cell_size

        # Helmet base
        helmet_points = [
            x0 + 15, y0 + 5,   # Top left
            x0 + 35, y0 + 5,   # Top right
            x0 + 40, y0 + 15,  # Right top curve
            x0 + 40, y0 + 30,  # Right side
            x0 + 35, y0 + 40,  # Bottom right
            x0 + 15, y0 + 40,  # Bottom left
            x0 + 10, y0 + 30,  # Left side
            x0 + 10, y0 + 15,  # Left top curve
        ]
        self.canvas.create_polygon(
            *helmet_points, fill='#C0C0C0', outline='black', tags='player'
        )

        # Visor
        visor_points = [
            x0 + 15, y0 + 20,
            x0 + 35, y0 + 20,
            x0 + 33, y0 + 25,
            x0 + 17, y0 + 25,
        ]
        self.canvas.create_polygon(
            *visor_points, fill='black', outline='black', tags='player'
        )

        # Eye slit
        self.canvas.create_line(
            x0 + 18, y0 + 22, x0 + 32, y0 + 22, fill='#FFD700', width=2, tags='player'
        )

        # Plume (red)
        plume_points = [
            x0 + 25, y0 - 5,   # Top of plume
            x0 + 30, y0 + 5,
            x0 + 25, y0 + 10,
            x0 + 20, y0 + 5,
        ]
        self.canvas.create_polygon(
            *plume_points, fill='red', outline='black', tags='player'
        )

        # Plume details
        self.canvas.create_line(
            x0 + 25, y0 - 5, x0 + 25, y0 + 10, fill='darkred', width=2, tags='player'
        )
        self.canvas.create_line(
            x0 + 22, y0, x0 + 28, y0, fill='darkred', width=2, tags='player'
        )

        # Helmet decorations
        self.canvas.create_arc(
            x0 + 10, y0 + 10, x0 + 40, y0 + 40, start=0, extent=180,
            style='arc', outline='black', tags='player'
        )
        self.canvas.create_line(
            x0 + 25, y0 + 5, x0 + 25, y0 + 40, fill='darkgray', dash=(4, 2), tags='player'
        )

        # Chin guard
        chin_guard_points = [
            x0 + 15, y0 + 40,
            x0 + 35, y0 + 40,
            x0 + 30, y0 + 45,
            x0 + 20, y0 + 45,
        ]
        self.canvas.create_polygon(
            *chin_guard_points, fill='#A9A9A9', outline='black', tags='player'
        )

        # Add rivets on the helmet
        for i in range(5):
            self.canvas.create_oval(
                x0 + 15 + i * 4, y0 + 30, x0 + 17 + i * 4, y0 + 32,
                fill='black', tags='player'
            )

        self.canvas.tag_raise('player')  # Ensure player is always on top

    def draw_treasure(self):
        x0, y0 = self.treas_x * self.cell_size, self.treas_y * self.cell_size
        x1, y1 = x0 + self.cell_size, y0 + self.cell_size

        # Draw a medieval treasure chest
        chest_x0 = x0 + 10
        chest_y0 = y0 + 20
        chest_x1 = x1 - 10
        chest_y1 = y1 - 10

        # Chest base
        self.canvas.create_rectangle(chest_x0, chest_y0, chest_x1, chest_y1, fill='#8B4513', outline='black', width=2, tags='treasure')

        # Chest lid
        self.canvas.create_arc(chest_x0, chest_y0 - 20, chest_x1, chest_y0 + 20, start=0, extent=180, fill='#A0522D', outline='black', width=2, tags='treasure')

        # Metal bands
        self.canvas.create_line(chest_x0, (chest_y0 + chest_y1) / 2, chest_x1, (chest_y0 + chest_y1) / 2, fill='black', width=2, tags='treasure')
        self.canvas.create_line((chest_x0 + chest_x1) / 2, chest_y0, (chest_x0 + chest_x1) / 2, chest_y1, fill='black', width=2, tags='treasure')

        # Lock
        self.canvas.create_oval(
            (chest_x0 + chest_x1) / 2 - 5, chest_y1 - 15,
            (chest_x0 + chest_x1) / 2 + 5, chest_y1 - 5,
            fill='gold', outline='black', tags='treasure'
        )

    def generate_coins(self):
        num_coins = random.randint(5, 15)
        possible_positions = [(i, j) for i in range(self.board_size) for j in range(self.board_size)
                              if (i, j) != (self.player_x, self.player_y) and
                                 (i, j) != (self.treas_x, self.treas_y) and
                                 (i, j) not in self.dragon_body]
        random.shuffle(possible_positions)
        self.coins = possible_positions[:num_coins]

    def draw_coins(self):
        self.canvas.delete('coin')
        for (i, j) in self.coins:
            x0, y0 = i * self.cell_size, j * self.cell_size
            # Draw coin
            self.canvas.create_oval(
                x0 + 15, y0 + 15, x0 + 35, y0 + 35,
                fill='gold', outline='black', tags='coin'
            )
            # Add coin details
            self.canvas.create_line(
                x0 + 20, y0 + 25, x0 + 30, y0 + 25,
                fill='black', width=2, tags='coin'
            )
            self.canvas.create_line(
                x0 + 25, y0 + 20, x0 + 25, y0 + 30,
                fill='black', width=2, tags='coin'
            )

    def key_pressed(self, event):
        key = event.keysym
        if key == 'w' and self.player_y > 0:
            self.player_y -= 1
        elif key == 's' and self.player_y < self.board_size - 1:
            self.player_y += 1
        elif key == 'a' and self.player_x > 0:
            self.player_x -= 1
        elif key == 'd' and self.player_x < self.board_size - 1:
            self.player_x += 1
        self.update_player()
        self.check_location()
        self.check_victory()

    def update_player(self):
        self.canvas.delete('player')
        self.draw_player()
        # Uncover the tile the player is currently on
        i, j = self.player_x, self.player_y
        self.canvas.delete(f'cover_{i}_{j}')

        # Check if player collected a coin
        if (i, j) in self.coins:
            self.coins.remove((i, j))
            self.knight_coins += 1
            self.coin_label.config(text=f"Coins Collected: {self.knight_coins}")
            # Remove the coin from the canvas
            self.draw_coins()

        # Check if treasure should be revealed
        if not self.treasure_visible and abs(self.player_x - self.treas_x) <= 1 and abs(self.player_y - self.treas_y) <= 1:
            self.treasure_visible = True
            self.draw_treasure()
            # Uncover the treasure tile
            self.canvas.delete(f'cover_{self.treas_x}_{self.treas_y}')

    def update_message_bar(self, new_message):
        self.message_label.config(text=new_message)

    def check_location(self):
        messages = []
        current_biome = None
        for biome in self.biomes:
            if (self.player_x, self.player_y) in biome['tiles']:
                current_biome = biome['type']
                if self.current_biome != current_biome:
                    if self.current_biome is not None:
                        messages.append(f"You have left the {self.current_biome} biome.")
                    messages.append(f"You have entered the {current_biome} biome.")
                else:
                    messages.append(f"You are in the {current_biome} biome.")
                break

        if self.current_biome and not current_biome:
            messages.append(f"You have left the {self.current_biome} biome and are now on an old cobblestone path.")
        elif not self.current_biome and not current_biome:
            messages.append("You are walking along an eroded cobblestone path.")

        if abs(self.player_x - self.treas_x) <= 2 and abs(self.player_y - self.treas_y) <= 2:
            if not self.treasure_message_shown:
                messages.append("You feel a strange presence... You must be close to the treasure!")
                self.treasure_message_shown = True
        else:
            self.treasure_message_shown = False

        if messages:
            self.update_message_bar("\n".join(messages))

        self.previous_biome = self.current_biome
        self.current_biome = current_biome

    def check_victory(self):
        if self.player_x == self.treas_x and self.player_y == self.treas_y:
            self.update_message_bar("✨ You Found the Treasure! ✨")
            self.display_end_message("✨ YOU FOUND THE TREASURE! ✨", 'gold', 'yellow')
            self.root.unbind("<KeyPress>")
            self.dragon_action_running = False

    def display_end_message(self, message, text_color, border_color):
        # Create a rectangle with border
        self.canvas.create_rectangle(
            self.window_width // 2 - 150, self.window_height // 2.5 - 50,
            self.window_width // 2 + 150, self.window_height // 2.5 + 50,
            fill='grey25', outline=border_color, width=5, tags='end_message'
        )
        # Add the message text
        self.canvas.create_text(
            self.window_width // 2, self.window_height // 2.5,
            text=message, font=('Terminal', 11), fill=text_color, tags='end_message'
        )

    def init_dragon_snake(self):
        # Start the dragon snake at bottom right corner 
        while True:
            x = (self.board_size - 1)
            y = (self.board_size - 1)
            if (x, y) != (self.player_x, self.player_y) and (x, y) != (self.treas_x, self.treas_y) and (x, y) not in self.coins:
                self.dragon_body = [(x, y)]
                self.dragon_direction = random.choice(['up', 'down', 'left', 'right'])
                break

    def draw_dragon_snake(self):
        self.canvas.delete('dragon')
        for index, (x, y) in enumerate(self.dragon_body):
            x0, y0 = x * self.cell_size, y * self.cell_size

            if index == 0:
                # Draw detailed dragon head
                self.draw_dragon_head(x0, y0, self.dragon_direction)
            else:
                # Draw dragon body segment with scales
                self.draw_dragon_body_segment(x0, y0)

        self.canvas.tag_raise('dragon')

    def draw_dragon_head(self, x0, y0, direction):
        # Adjust the dragon head based on the direction
        # Create a more detailed dragon head with horns, eyes, mouth, and scales
        head_size = self.cell_size
        half_size = head_size // 2

        if direction == 'up':
            # Coordinates for upward-facing dragon head
            head_points = [
                x0 + half_size, y0,                    # Nose tip
                x0 + head_size - 5, y0 + half_size,    # Right cheek
                x0 + half_size, y0 + head_size - 5,    # Chin
                x0 + 5, y0 + half_size                 # Left cheek
            ]
            eye_coords = (x0 + half_size - 10, y0 + half_size - 15, x0 + half_size - 5, y0 + half_size - 10)
            horn_points = [
                x0 + half_size - 5, y0 + 5,
                x0 + half_size - 10, y0 - 10,
                x0 + half_size + 5, y0 - 10,
                x0 + half_size + 5, y0 + 5
            ]
            mouth_line = (x0 + half_size - 10, y0 + head_size - 15, x0 + half_size + 10, y0 + head_size - 15)
        elif direction == 'down':
            # Coordinates for downward-facing dragon head
            head_points = [
                x0 + half_size, y0 + head_size,        # Nose tip
                x0 + head_size - 5, y0 + half_size,    # Right cheek
                x0 + half_size, y0 + 5,                # Forehead
                x0 + 5, y0 + half_size                 # Left cheek
            ]
            eye_coords = (x0 + half_size + 5, y0 + half_size + 10, x0 + half_size + 10, y0 + half_size + 15)
            horn_points = [
                x0 + half_size - 5, y0 + head_size - 5,
                x0 + half_size - 10, y0 + head_size + 10,
                x0 + half_size + 5, y0 + head_size + 10,
                x0 + half_size + 5, y0 + head_size - 5
            ]
            mouth_line = (x0 + half_size - 10, y0 + 15, x0 + half_size + 10, y0 + 15)
        elif direction == 'left':
            # Coordinates for left-facing dragon head
            head_points = [
                x0, y0 + half_size,                    # Nose tip
                x0 + half_size, y0 + head_size - 5,    # Lower jaw
                x0 + head_size - 5, y0 + half_size,    # Back of head
                x0 + half_size, y0 + 5                 # Upper jaw
            ]
            eye_coords = (x0 + half_size - 15, y0 + half_size - 10, x0 + half_size - 10, y0 + half_size - 5)
            horn_points = [
                x0 + 5, y0 + half_size - 5,
                x0 - 10, y0 + half_size - 10,
                x0 - 10, y0 + half_size + 5,
                x0 + 5, y0 + half_size + 5
            ]
            mouth_line = (x0 + head_size - 15, y0 + half_size - 10, x0 + head_size - 15, y0 + half_size + 10)
        elif direction == 'right':
            # Coordinates for right-facing dragon head
            head_points = [
                x0 + head_size, y0 + half_size,        # Nose tip
                x0 + half_size, y0 + head_size - 5,    # Lower jaw
                x0 + 5, y0 + half_size,                # Back of head
                x0 + half_size, y0 + 5                 # Upper jaw
            ]
            eye_coords = (x0 + half_size + 10, y0 + half_size - 15, x0 + half_size + 15, y0 + half_size - 10)
            horn_points = [
                x0 + head_size - 5, y0 + half_size - 5,
                x0 + head_size + 10, y0 + half_size - 10,
                x0 + head_size + 10, y0 + half_size + 5,
                x0 + head_size - 5, y0 + half_size + 5
            ]
            mouth_line = (x0 + 15, y0 + half_size - 10, x0 + 15, y0 + half_size + 10)

        # Draw dragon head
        self.canvas.create_polygon(
            head_points, fill='#006400', outline='black', tags='dragon'
        )
        # Draw dragon eye
        self.canvas.create_oval(
            *eye_coords, fill='yellow', outline='black', tags='dragon'
        )
        # Draw dragon horn
        self.canvas.create_polygon(
            horn_points, fill='#A9A9A9', outline='black', tags='dragon'
        )
        # Draw dragon mouth
        self.canvas.create_line(
            *mouth_line, fill='red', width=2, tags='dragon'
        )
        # Add scales to the head
        for i in range(3):
            self.canvas.create_arc(
                x0 + 10 + i*10, y0 + 10, x0 + 20 + i*10, y0 + 20,
                start=0, extent=180, fill='#228B22', outline='black', tags='dragon'
            )

    def draw_dragon_body_segment(self, x0, y0):
        # Draw dragon body segment with scales
        self.canvas.create_rectangle(
            x0, y0, x0 + self.cell_size, y0 + self.cell_size,
            fill='#006400', outline='black', tags='dragon'
        )
        # Add scales pattern
        for i in range(2):
            for j in range(2):
                self.canvas.create_arc(
                    x0 + 10 + i*15, y0 + 10 + j*15, x0 + 25 + i*15, y0 + 25 + j*15,
                    start=0, extent=180, fill='#228B22', outline='black', tags='dragon'
                )

    def dragon_action(self):
        if not hasattr(self, 'dragon_action_running') or not self.dragon_action_running:
            return
        self.move_dragon_snake()
        self.dragon_breathe_fire()
        self.root.after(500, self.dragon_action)

    def move_dragon_snake(self):
        # Remove previous dragon drawing
        self.canvas.delete('dragon')

        # Determine the dragon's target (coin or knight)
        if self.coins:
            # Find the nearest coin
            head_x, head_y = self.dragon_body[0]
            nearest_coin = min(self.coins, key=lambda c: abs(c[0] - head_x) + abs(c[1] - head_y))
            target_x, target_y = nearest_coin
        else:
            # No coins left, target the knight
            target_x, target_y = self.player_x, self.player_y

        head_x, head_y = self.dragon_body[0]

        possible_directions = []
        if head_x < target_x and self.dragon_direction != 'left':
            possible_directions.append('right')
        elif head_x > target_x and self.dragon_direction != 'right':
            possible_directions.append('left')
        if head_y < target_y and self.dragon_direction != 'up':
            possible_directions.append('down')
        elif head_y > target_y and self.dragon_direction != 'down':
            possible_directions.append('up')

        if possible_directions:
            self.dragon_direction = random.choice(possible_directions)
        else:
            # If no possible directions, continue in the current direction
            pass

        # Calculate new head position
        dx, dy = 0, 0
        if self.dragon_direction == 'up':
            dy = -1
        elif self.dragon_direction == 'down':
            dy = 1
        elif self.dragon_direction == 'left':
            dx = -1
        elif self.dragon_direction == 'right':
            dx = 1

        new_head_x = head_x + dx
        new_head_y = head_y + dy

        # Check boundaries
        if 0 <= new_head_x < self.board_size and 0 <= new_head_y < self.board_size:
            # Update the body
            self.dragon_body.insert(0, (new_head_x, new_head_y))

            # Check if dragon collected a coin
            if (new_head_x, new_head_y) in self.coins:
                self.coins.remove((new_head_x, new_head_y))
                # Dragon grows by one tile
                self.dragon_coins_collected += 1
                # Remove the coin from the canvas
                self.draw_coins()
            else:
                # Remove the tail segment unless the dragon has collected coins equal to its current length minus initial length
                if len(self.dragon_body) > 3 + self.dragon_coins_collected:
                    self.dragon_body.pop()
        else:
            # Hit the boundary, reverse direction
            if self.dragon_direction == 'up':
                self.dragon_direction = 'down'
            elif self.dragon_direction == 'down':
                self.dragon_direction = 'up'
            elif self.dragon_direction == 'left':
                self.dragon_direction = 'right'
            elif self.dragon_direction == 'right':
                self.dragon_direction = 'left'

        # Redraw the dragon
        self.draw_dragon_snake()

        # Check for collision with knight
        if self.is_knight_in_dragon():
            self.knight_caught_by_dragon()

    def is_knight_in_dragon(self):
        if (self.player_x, self.player_y) in self.dragon_body:
            return True
        return False

    def knight_caught_by_dragon(self):
        self.update_message_bar("The dragon has caught you! Game Over.")
        self.display_end_message("💀 GAME OVER! Mushed! 💀", 'dark green', 'dark green')
        # Unbind keys to stop the game
        self.root.unbind("<KeyPress>")
        # Stop the dragon's actions
        self.dragon_action_running = False

    def dragon_breathe_fire(self):
        # Remove previous fire
        self.canvas.delete('fire')

        head_x, head_y = self.dragon_body[0]
        dx, dy = 0, 0
        if self.dragon_direction == 'up':
            dx, dy = 0, -1
        elif self.dragon_direction == 'down':
            dx, dy = 0, 1
        elif self.dragon_direction == 'left':
            dx, dy = -1, 0
        elif self.dragon_direction == 'right':
            dx, dy = 1, 0

        # Fire extends 2 tiles ahead
        self.fire_length = 2 * self.cell_size  # Total fire length in pixels
        self.fire_progress = 0  # Fire progress in pixels
        self.fire_increment = self.cell_size // 16  # Increment per frame
        self.fire_direction = (dx, dy)
        self.fire_origin = (head_x * self.cell_size, head_y * self.cell_size)
        self.fire_pixels = []  # To store fire segments for deletion
        self.fire_animation()

    def fire_animation(self):
        if self.fire_progress >= self.fire_length:
            # Fire animation complete
            # Remove the fire after some time
            self.root.after(100, self.clear_fire)
            return

        # Calculate current fire end position
        fx0, fy0 = self.fire_origin
        dx, dy = self.fire_direction
        increment = self.fire_progress + self.fire_increment
        fx1 = fx0 + dx * increment
        fy1 = fy0 + dy * increment

        # Draw fire segment
        self.draw_billowing_fire(fx0, fy0, fx1, fy1, dx, dy)

        # Update fire progress
        self.fire_progress += self.fire_increment

        # Check if knight is hit by fire
        knight_x = self.player_x * self.cell_size + self.cell_size // 2
        knight_y = self.player_y * self.cell_size + self.cell_size // 2
        if self.is_point_in_fire(knight_x, knight_y):
            self.knight_hit_by_fire()

        # Schedule next frame
        self.root.after(50, self.fire_animation)

    def draw_billowing_fire(self, x0, y0, x1, y1, dx, dy):
        # Determine fire colors
        colors = ['#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#FFFF00']

        # Calculate the fire width based on progress to create a billowing effect
        fire_width = self.cell_size * (0.2 + 0.3 * (self.fire_progress / self.fire_length))

        # Create a polygon representing the fire
        if dx == 0:
            # Vertical fire
            left = x0 - fire_width / 2
            right = x0 + self.cell_size + fire_width / 2
            if dy > 0:
                # Fire going down
                points = [
                    (x0 + self.cell_size / 2, y0 + self.cell_size / 2),
                    (left, y0 + self.cell_size / 2 + self.fire_progress),
                    (right, y0 + self.cell_size / 2 + self.fire_progress),
                ]
            else:
                # Fire going up
                points = [
                    (x0 + self.cell_size / 2, y0 + self.cell_size / 2),
                    (left, y0 + self.cell_size / 2 - self.fire_progress),
                    (right, y0 + self.cell_size / 2 - self.fire_progress),
                ]
        else:
            # Horizontal fire
            top = y0 - fire_width / 2
            bottom = y0 + self.cell_size + fire_width / 2
            if dx > 0:
                # Fire going right
                points = [
                    (x0 + self.cell_size / 2, y0 + self.cell_size / 2),
                    (x0 + self.cell_size / 2 + self.fire_progress, top),
                    (x0 + self.cell_size / 2 + self.fire_progress, bottom),
                ]
            else:
                # Fire going left
                points = [
                    (x0 + self.cell_size / 2, y0 + self.cell_size / 2),
                    (x0 + self.cell_size / 2 - self.fire_progress, top),
                    (x0 + self.cell_size / 2 - self.fire_progress, bottom),
                ]

        # Draw the fire polygon
        color = random.choice(colors)
        self.fire_pixels.append(
            self.canvas.create_polygon(
                points, fill=color, outline='', tags='fire'
            )
        )

    def is_point_in_fire(self, x, y):
        # Check if a point is within the fire area
        fx0, fy0 = self.fire_origin
        dx, dy = self.fire_direction
        fx1 = fx0 + dx * self.fire_progress
        fy1 = fy0 + dy * self.fire_progress

        # Create a rectangle representing the fire area
        if dx == 0:
            # Vertical fire
            min_y = min(fy0, fy1)
            max_y = max(fy0 + self.cell_size, fy1 + self.cell_size)
            left = fx0 - self.cell_size // 2
            right = fx0 + self.cell_size * 1.5
            if left <= x <= right and min_y <= y <= max_y:
                return True
        elif dy == 0:
            # Horizontal fire
            min_x = min(fx0, fx1)
            max_x = max(fx0 + self.cell_size, fx1 + self.cell_size)
            top = fy0 - self.cell_size // 2
            bottom = fy0 + self.cell_size * 1.5
            if top <= y <= bottom and min_x <= x <= max_x:
                return True
        return False

    def clear_fire(self):
        self.canvas.delete('fire')
        self.fire_pixels = []

    def knight_hit_by_fire(self):
        self.update_message_bar("The dragon's fire has consumed you! Game Over.")
        self.display_end_message("🔥 GAME OVER! Crispy. 🔥", 'red', 'red')
        # Unbind keys to stop the game
        self.root.unbind("<KeyPress>")
        # Stop the dragon's actions
        self.dragon_action_running = False

if __name__ == "__main__":
    root = tk.Tk()
    game = TreasureHuntGame(root)
    root.mainloop()
