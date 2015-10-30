import FWCore.ParameterSet.Config as cms

ttbarselectionproducer = cms.EDProducer("TTbarSelectionProducer",
                                        verbose          = cms.int32(0),
                                        triggerColl      = cms.InputTag("TriggerResults","","HLT"),
                                        metFilters       = cms.VInputTag(cms.InputTag('TriggerResults','','RECO'),
                                                                         cms.InputTag('TriggerResults','','PAT')),
                                        RecoHBHENoiseFilter = cms.InputTag('hcalnoise','','RECO'),
                                        metFiltersToApply= cms.vstring("Flag_HBHENoiseFilter","Flag_CSCTightHaloFilter","Flag_goodVertices","Flag_eeBadScFilter"),
                                        vtxColl          = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        #cf https://twiki.cern.ch/twiki/bin/view/CMS/TopTrigger
                                        trigNamesToSel   = cms.vstring('Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL',
                                                                       'Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL',
                                                                       'Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ',
                                                                       'Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'
                                                                       ),
                                        trigChannels     = cms.vint32(11*13,
                                                                      11*13,
                                                                      11*11,
                                                                      13*13),
                                        doTrigSel        = cms.bool(True),
                                        electronColl     = cms.InputTag("slimmedElectrons"),
                                        conversions      = cms.InputTag("reducedEgamma:reducedConversions"),
                                        electronIdMap    = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium"),
                                        electron_cut_pt  = cms.double(20),
                                        electron_cut_eta = cms.double(2.4),
                                        electron_cut_iso = cms.double(0.11),
                                        muonColl         = cms.InputTag("slimmedMuons"),
                                        muon_cut_pt      = cms.double(20),
                                        muon_cut_eta     = cms.double(2.4),
                                        muon_cut_iso     = cms.double(0.12),
                                        jetColl          = cms.InputTag("slimmedJets"),
                                        jet_cut_pt       = cms.double(20),
                                        jet_cut_eta      = cms.double(2.5),
                                        metColl          = cms.InputTag("slimmedMETsNoHF"),
                                        met_cut          = cms.double(0)
                                        )
