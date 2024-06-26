import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.texture = texture
        self.texture_rect = texture_rect

        self.moves = []
        self.moved =  False

        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.set_texture()
    
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f"assets/images/imgs-{size}px/{self.color}_{self.name}.png"
        )

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []

class Pawn(Piece):
    
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        self.en_passant = False
        super().__init__(name="Pawn", color=color, value=1.0)

class Knight(Piece):
    
    def __init__(self, color):
        super().__init__(name="Knight", color=color, value=3.0)

class Bishop(Piece):
    
    def __init__(self, color):
        super().__init__(name="Bishop", color=color, value=3.001)

class Rook(Piece):
    
    def __init__(self, color):
        super().__init__(name="Rook", color=color, value=5.0)

class Queen(Piece):
    
    def __init__(self, color):
        super().__init__(name="Queen", color=color, value=9.0)

class King(Piece):
    
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__(name="King", color=color, value=9999.0)