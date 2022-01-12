#!/usr/bin/env python
import ROOT
from ROOT import TFile, TCanvas

#################################################################################

fiData = TFile.Open("root://cmseos.fnal.gov//store/user/cmsdas/2022/long_exercises/TopMass/MuonEG_2016Hv2.root", "READ")
treeData = fiData.Get("data")

c1 = TCanvas("canvas 1", "c1", 600, 600)
c1.cd()

treeData.Draw("Jet_pt", "Jet_CombIVF>0.605")
c1.SaveAs("plotData.png")

#################################################################################

fiMC = TFile.Open("root://cmseos.fnal.gov//store/user/cmsdas/2022/long_exercises/TopMass/TTJets.root", "READ")
treeMC = fiMC.Get("data")

c2 = TCanvas("canvas 2", "c2", 600, 600)
c2.cd()

treeMC.Draw("Jet_genpt", "abs(Jet_flavour)==5")
c2.SaveAs("plotMC.png")

##################################################################################
##################################################################################

mcinF=TFile.Open("root://cmseos.fnal.gov///store/user/cmsdas/2022/long_exercises/TopMass/TTJets.root")
mct=mcinF.Get("data")

c3 = TCanvas("canvas 3", "c3", 600, 600)
c3.cd()

mct.Draw("Jet_genpt")
mct.Draw("Jet_genpt", "abs(Jet_flavour)==5", "e1same")
c3.SaveAs("plotMC_auto.png")

##################################################################################

c4 = TCanvas("canvas 4", "c4", 600, 600)
c4.cd()

mct.Draw("(Jet_pt-Jet_genpt)/Jet_genpt","abs(Jet_flavour)==5 && Jet_genpt > 0")
c4.SaveAs("plotRES.png")

##################################################################################

c5 = TCanvas("canvas 5", "c5", 600, 600)
c5.cd()

mct.Draw("Lepton_pt","abs(Lepton_id)==11 && Lepton_pt < 200")
mct.Draw("Lepton_pt","abs(Lepton_gid)==11 && Lepton_pt < 200", "e1same")
c5.SaveAs("plotLEPTON.png")

##################################################################################

c6 = TCanvas("canvas 6", "c6", 600, 600)
c6.cd()

mct.Draw("Lepton_pt","abs(Lepton_id)==13 && Lepton_pt < 200")
mct.Draw("Lepton_pt","abs(Lepton_gid)==13 && Lepton_pt < 200", "e1same")
c6.SaveAs("plotLEPTMUON.png")
