from mvg_api.mvg_api_requests import *

from colr import color
from texttable import Texttable

import sys
import os

MVG_BG = "#2a4779"
MVG_FG = "#ffffff"


class Departure:
    
    def __init__( self, json ):
        self.label = json["label"]
        self.destination = json["destination"]
        self.departure_time_minutes = json["departureTimeMinutes"]
        self.line_background_color = json["lineBackgroundColor"]

    def get_label_colored(self):
        label = color(self.label, fore="#fff", back=self.line_background_color)
        return label

    def get_destination(self):
        return self.destination

    def get_departure_time_min(self):
        return self.departure_time_minutes
    
    def __str__(self):
        label = self.get_label_colored()
        direction = self.get_destination()
        departure_min = self.departure_time_minutes

        return label + "\t" + direction + "\t" + str(departure_min)
        

def display_title_bar():
    """ Print a title bar. """

    color_it_mvg = lambda x: color(x, fore=MVG_FG, back=MVG_BG)
    bar_mvg_colored = color_it_mvg("*" * 48)
    fifteen_stars = "*" * 15

    print(bar_mvg_colored)
    print(color_it_mvg(fifteen_stars + " MVG - Departures " + fifteen_stars))
    print(bar_mvg_colored + "\n")


def display_departures(station_name, limit=20):
    departuresJSON = get_departures_by_name(station_name)
    departuresJSON = departuresJSON[:limit]

    departures = [ Departure(i) for i in departuresJSON ]
    
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype( ['t', 't', 'i'])
    table.set_cols_align( ['l', 'l', 'r'] )
    
    rows = []
    rows.append(['\x1b[38;5;231m\x1b[48;5;23mline\x1b[0m', 'destination', 'departure (min)'])
    for dep in departures:
        rows.append( [dep.get_label_colored(), dep.destination, dep.departure_time_minutes] )
    table.add_rows(rows)
    print( color(table.draw(), fore=MVG_FG, back=MVG_BG) )
    


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(prog="mvg")
    parser.add_argument("--recent", "-r", action="store_true")
    parser.add_argument("--departures", "-d")
    args = parser.parse_args()

    recents_file_path = os.path.join(os.getcwd(), "recent.txt")

    if args.recent:
        with open(recents_file_path, "r") as recent:
            display_departures(recent.read())
    elif args.departures:
        display_departures(args.departures)
        with open(recents_file_path, "w") as recent:
            recent.write(args.departures)
    else:
        display_departures("Studentenstadt")
