import FWCore.ParameterSet.Config as cms

## PFproducer for particle flow for PFCaloJets
#disable tracks and also input blocks are hltParticleFlowBlock

hltParticleFlow = cms.EDProducer("PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double(0.034),
    minPtForPostCleaning = cms.double(20.0),
    pf_nsigma_ECAL = cms.double(0.0),
    GedPhotonValueMap = cms.InputTag(""),
    sumPtTrackIsoForPhoton = cms.double(2.0),
    metFactorForFakes = cms.double(4.0),
    muon_HO = cms.vdouble(0.9, 0.9),
    electron_missinghits = cms.uint32(1),
    metSignificanceForCleaning = cms.double(3.0),
    usePFPhotons = cms.bool(False),
    dptRel_DispVtx = cms.double(10.0),
    nTrackIsoForEgammaSC = cms.uint32(2),
    pf_nsigma_HCAL = cms.double(1.0),
    cosmicRejectionDistance = cms.double(1.0),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False),
    nsigma_TRACK = cms.double(1.0),
    useEGammaSupercluster = cms.bool(False),
    eventFractionForCleaning = cms.double(0.5),
    usePFDecays = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    eventFractionForRejection = cms.double(0.8),
    pf_locC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterLCorr_14Dec2011.root'),
    photon_MinEt = cms.double(10.0),
    usePFNuclearInteractions = cms.bool(False),
    maxSignificance = cms.double(2.5),
    electron_iso_mva_endcap = cms.double(-0.1075),
    electron_noniso_mvaCut = cms.double(-0.1),
    pf_convID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt'),
    calibHF_eta_step = cms.vdouble(0.0, 2.9, 3.0, 3.2, 4.2, 
        4.4, 4.6, 4.8, 5.2, 5.4),
    ptErrorScale = cms.double(8.0),
    minSignificance = cms.double(2.5),
    minMomentumForPunchThrough = cms.double(100.0),
    pf_conv_mvaCut = cms.double(0.0),
    useCalibrationsFromDB = cms.bool(True),
    usePFElectrons = cms.bool(False),
    blocks = cms.InputTag("hltParticleFlowBlock"),
    photon_combIso = cms.double(10.0),
    electron_iso_mva_barrel = cms.double(-0.1875),
    postHFCleaning = cms.bool(False),
    factors_45 = cms.vdouble(10.0, 100.0),
    cleanedHF = cms.VInputTag(cms.InputTag("particleFlowRecHitHF","Cleaned"), cms.InputTag("particleFlowClusterHF","Cleaned")),
    coneEcalIsoForEgammaSC = cms.double(0.3),
    egammaElectrons = cms.InputTag(""),
    photon_SigmaiEtaiEta_barrel = cms.double(0.0125),
    calibHF_b_HADonly = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    minPixelHits = cms.int32(1),
    maxDPtOPt = cms.double(1.0),
    useHO = cms.bool(True),
    pf_electron_output_col = cms.string('electrons'),
    debug = cms.untracked.bool(False),
    GedElectronValueMap = cms.InputTag("gedGsfElectronsTmp"),
    useVerticesForNeutral = cms.bool(False),
    trackQuality = cms.string('highPurity'),
    PFEGammaCandidates = cms.InputTag(""),
    sumPtTrackIsoSlopeForPhoton = cms.double(0.001),
    coneTrackIsoForEgammaSC = cms.double(0.3),
    minDeltaMet = cms.double(0.4),
    pt_Error = cms.double(1.0),
    useProtectionsForJetMET = cms.bool(False),
    metFactorForRejection = cms.double(4.0),
    sumPtTrackIsoForEgammaSC_endcap = cms.double(4.0),
    calibHF_use = cms.bool(False),
    verbose = cms.untracked.bool(False),
    usePFConversions = cms.bool(False),
    calibPFSCEle_endcap = cms.vdouble(1.153, -16.5975, 5.668, -0.1772, 16.22, 
        7.326, 0.0483, -4.068, 9.406),
    metFactorForCleaning = cms.double(4.0),
    eventFactorForCosmics = cms.double(10.0),
    minSignificanceReduction = cms.double(1.4),
    minEnergyForPunchThrough = cms.double(100.0),
    minTrackerHits = cms.int32(8),
    iCfgCandConnector = cms.PSet(
        nuclCalibFactors = cms.vdouble(0.8, 0.15, 0.5, 0.5, 0.05),
        ptErrorSecondary = cms.double(1.0),
        bCalibPrimary = cms.bool(True),
        bCorrect = cms.bool(True),
        dptRel_MergedTrack = cms.double(5.0),
        dptRel_PrimaryTrack = cms.double(10.0)
    ),
    rejectTracks_Bad = cms.bool(False),
    pf_electronID_crackCorrection = cms.bool(False),
    sumPtTrackIsoForEgammaSC_barrel = cms.double(4.0),
    calibHF_a_EMonly = cms.vdouble(0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 
        0.89718, 0.98674, 1.4681, 1.458, 1.458),
    pf_Res_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes_14Dec2011.root'),
    metFactorForHighEta = cms.double(25.0),
    minHFCleaningPt = cms.double(5.0),
    muon_HCAL = cms.vdouble(3.0, 3.0),
    pf_electron_mvaCut = cms.double(-0.1),
    ptFactorForHighEta = cms.double(2.0),
    sumEtEcalIsoForEgammaSC_endcap = cms.double(2.0),
    maxDeltaPhiPt = cms.double(7.0),
    pf_electronID_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
    muons = cms.InputTag(""),
    calibHF_b_EMHAD = cms.vdouble(1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 
        0.94348, 0.9437, 1.0034, 1.0444, 1.0444),
    pf_GlobC_mvaWeightFile = cms.string('RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr_14Dec2011.root'),
    photon_HoE = cms.double(0.05),
    sumEtEcalIsoForEgammaSC_barrel = cms.double(1.0),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(0.9, 6.5, -0.0692932, 0.101776, 0.995338, 
        -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 
        0.923165, 0.000474665, 1.10782),
    punchThroughFactor = cms.double(3.0),
    algoType = cms.uint32(0),
    electron_iso_combIso_barrel = cms.double(10.0),
    postMuonCleaning = cms.bool(False),
    calibPFSCEle_barrel = cms.vdouble(1.004, -1.536, 22.88, -1.467, 0.3555, 
        0.6227, 14.65, 2051, 25, 0.9932, 
        -0.5444, 0, 0.5438, 0.7109, 7.645, 
        0.2904, 0),
    electron_protectionsForJetMET = cms.PSet(
        maxTrackPOverEele = cms.double(1.0),
        maxEcalEOverP_2 = cms.double(0.2),
        maxHcalEOverEcalE = cms.double(0.1),
        maxEcalEOverP_1 = cms.double(0.5),
        maxHcalEOverP = cms.double(1.0),
        maxEeleOverPoutRes = cms.double(0.5),
        maxEcalEOverPRes = cms.double(0.2),
        maxHcalE = cms.double(10.0),
        maxEeleOverPout = cms.double(0.2),
        maxNtracks = cms.double(3.0),
        maxEleHcalEOverEcalE = cms.double(0.1),
        maxDPhiIN = cms.double(0.1),
        maxE = cms.double(50.0)
    ),
    electron_iso_pt = cms.double(10.0),
    isolatedElectronID_mvaWeightFile = cms.string('RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml'),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    X0_Map = cms.string('RecoParticleFlow/PFProducer/data/allX0histos.root'),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(0.6, 6, -0.0255975, 0.0576727, 0.975442, 
        -0.000546394, 1.26147, 25, -0.02025, 0.04537, 
        0.9728, -0.0008962, 1.172),
    electron_iso_combIso_endcap = cms.double(10.0),
    punchThroughMETFactor = cms.double(4.0),
    metSignificanceForRejection = cms.double(4.0),
    photon_protectionsForJetMET = cms.PSet(
        sumPtTrackIsoSlope = cms.double(0.001),
        sumPtTrackIso = cms.double(4.0)
    ),
    usePhotonReg = cms.bool(False),
    dzPV = cms.double(0.2),
    calibHF_a_EMHAD = cms.vdouble(1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 
        0.98504, 1.00802, 1.0593, 1.4576, 1.4576),
    useRegressionFromDB = cms.bool(True),
    muon_ECAL = cms.vdouble(0.5, 0.5),
    usePFSCEleCalib = cms.bool(False)
)

