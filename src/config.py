class Config:
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    SCREEN_TITLE = "PicPin - Dungeon Tool"

    # Counters
    COUNTER_SCALE = 0.6
    COUNTER_HEIGHT = 140 * COUNTER_SCALE
    COUNTER_WIDTH = 140 * COUNTER_SCALE

    # Matt
    MAT_PERCENT_OVERSIZE = 1.25
    MAT_HEIGHT = int(COUNTER_HEIGHT * MAT_PERCENT_OVERSIZE)
    MAT_WIDTH = int(COUNTER_WIDTH * MAT_PERCENT_OVERSIZE)

    # How big is the mat we'll place the card on?
    MAT_PERCENT_OVERSIZE = 1.25
    MAT_HEIGHT = int(COUNTER_HEIGHT * MAT_PERCENT_OVERSIZE)
    MAT_WIDTH = int(COUNTER_WIDTH * MAT_PERCENT_OVERSIZE)

    # How much space do we leave as a gap between the mats?
    # Done as a percent of the mat size.
    VERTICAL_MARGIN_PERCENT = 0.10
    HORIZONTAL_MARGIN_PERCENT = 0.10

    # The Y of the bottom row (2 piles)
    BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

    # The X of where to start putting things on the left side
    START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

    # How far apart each pile goes
    X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT