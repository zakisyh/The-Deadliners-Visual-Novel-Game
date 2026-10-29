# ==================================================================================================
# THE DEADLINERS - WEBSITE PROGRESS SYSTEM
# ==================================================================================================

# Nilai awal progres website (0-100)
default website_progress = 0


# ==================================================================================================
# WEBSITE PROGRESS BAR
# ==================================================================================================

screen website_progress_hud():

    zorder 100

    frame:
        xalign 0.98
        yalign 0.02

        xpadding 15
        ypadding 12

        background Solid("#17212DDD")

        vbox:
            spacing 8

            text "Website Progress: [website_progress]%":
                size 20
                color "#FFFFFF"

            bar:
                value AnimatedValue(
                    website_progress,
                    100,
                    delay=0.5
                )

                xsize 260
                ysize 16

                left_bar Solid("#58B8DC")
                right_bar Solid("#343B48")
