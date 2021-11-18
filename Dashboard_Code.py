# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:25:01 2021

@author: CDarden
"""

# https://www.youtube.com/watch?v=iAXwlrtBUEY

import plotly.graph_objects as go
import dash
import dash_html_components as html

app = dash.Dash()       

# define HTML component
app.layout = html.Div (children = [html.Div("Injection Molding Data Analysis", style = {
                                                        "color" : "black",
                                                        "font-size" : "50px",
                                                        "background-color" : "DimGrey",
                                                        "border-style" : "solid",
                                                        "text-align" : "center",
                                                        "display" : "inline-block",
                                                        "height" : "70px",
                                                        "width" : "80%"
                                                        }),
                
                        html.Div("LOGO", style = {
                                                        "color" : "white",
                                                        "font-size" : "50px",
                                                        "background-color" : "darkblue",
                                                        "border-style" : "solid",
                                                        "text-align" : "center",
                                                        "display" : "inline-block",
                                                        "height" : "70px",
                                                        "width" : "19%"
                                                        }),
                        
                       
                        html.Div("Part Number:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        
                        html.Div("Part Name:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "hsl(184, 6%, 72%)",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                                                
                        html.Div("Run Start:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Run Stop:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "hsl(184, 6%, 72%)",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        html.Div("Total Cycles:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Average Cycle Time:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Yield:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        html.Div("Defects:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "Khaki",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "900px",
                                                        "width" : "99%"
                                                        }),])

if __name__ == '__main__':
    app.run_server()
    

