# ============================================
# THE DEADLINERS - HUD SYSTEM
# ============================================
# Semua nilai HUD disimpan di sini
default website_progress = 0
default stress_level = 0
default days_left = 90

# Mengatur apakah HUD sedang ditampilkan.
default hud_visible = False

# ============================================
# AUTOMATIC OVERLAY
# ============================================
init python:
    if "deadliners_hud" not in config.overlay_screens:
        config.overlay_screens.append("deadliners_hud")


# ============================================
# HUD DISPLAY
# ============================================
screen deadliners_hud():

    zorder 100

    if hud_visible:

        frame:
            xalign 0.985
            yalign 0.025

            background Solid("#111820DD")
            xpadding 18
            ypadding 14

            vbox:
                xsize 235
                spacing 11

                # HEADER
                hbox:
                    xfill True

                    text "THE DEADLINERS":
                        size 15
                        bold True
                        color "#E5EAF0"

                    null width 10

                # COUNTDOWN
                text "[days_left] DAYS LEFT":
                    size 20
                    bold True
                    color "#F2F4F7"

                null height 2

                # WEBSITE PROGRESS
                hbox:
                    xfill True

                    text "WEBSITE":
                        size 13
                        color "#BFC9D4"

                    text "[website_progress]%":
                        size 13
                        bold True
                        color "#E5EAF0"
                        xalign 1.0

                bar:
                    value AnimatedValue(
                        website_progress, 100, delay=0.35
                    )

                    xsize 235
                    ysize 9

                    left_bar Solid("#648FAF")
                    right_bar Solid("#303D4A")
                    thumb None

                null height 2

                # STRESS
                hbox:
                    xfill True

                    text "STRESS":
                        size 13
                        color "#BFC9D4"

                    text "[stress_level]%":
                        size 13
                        bold True
                        color "#E5EAF0"
                        xalign 1.0

                bar:
                    value AnimatedValue(
                        stress_level, 100, delay=0.35
                    )

                    xsize 235
                    ysize 9

                    left_bar Solid("#CB806E")
                    right_bar Solid("#303D4A")
                    thumb None
