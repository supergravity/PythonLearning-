#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=2 ft=python et:

# Author          : Po-Hsun Chen (pohsun.chen.hep@gmail.com)
# Last Modified   : 29 Sep 2017 16:53 

from ROOT import gROOT
from ROOT import TChain
from ROOT import TCanvas,TH1F


if __name__ == "__main__":
    gROOT.LoadMacro("functionWgt.cc")
    from ROOT import wgt
    print wgt

    ch = TChain("tree")
    ch.Add("./randomTreeXYZ.root")
    canvas = TCanvas()
    h1 = TH1F("h1","",10,0,10);
    ch.Draw("xx >> h1", "(xx<10)*wgt(xx,yy)")
    canvas.Print("functionWgt.jpg")

