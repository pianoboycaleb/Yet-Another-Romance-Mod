label mod_script:
    scene bg bedroom
    stop music
    "test"
    if not persistent.test2:
        $ test2.unlock()
        $ persistent.test2 = True
    "hey"
    "you"
    "how"
    "are"
    "you"
    "doin"
    return