#!/usr/bin/env python
# -*- coding: utf-8 -*-


# The following three format element drive the INI attributes
FILENAME_FORMAT = '%(variable_id)s_%(table_id)s_%(source_id)s_%(experiment_id)s_%(member_id)s_%(grid_label)s[_%(period_start)s-%(period_end)s].nc'
DIRECTORY_FORMAT = '%(root)s/%(mip_era)s/%(activity_drs)s/%(institution_id)s/%(source_id)s/%(experiment_id)s/%(member_id)s/%(table_id)s/%(variable_id)s/%(grid_label)s/%(version)s'
DATASET_ID = '%(mip_era)s.%(activity_drs)s.%(institution_id)s.%(source_id)s.%(experiment_id)s.%(member_id)s.%(table_id)s.%(variable_id)s.%(grid_label)s'

# Optional dataset name format
DATASET_FORMAT = 'mip_era=%(mip_era)s, source_id=%(source_id)s, experiment=%(experiment_title)s, member_id=%(member_id)s, variable=%(variable_id)s, version=%(version)s'  # SKA - this hasn't been working, perhaps done for cmip5 custom?

# netCDF global attributes to extract in addition of DRS facets
EXTRACT_GLOBAL_NC = ['frequency',
                     'realm',
                     'product',
                     'nominal_resolution',
                     'source_type',
                     'grid',
                     'creation_date',
                     'variant_label',
                     'sub_experiment_id',
                     'further_info_url',
                     'activity_id',
                     'data_specs_version']

# netCDF variable to exclude from THREDDS
THREDDS_EXCLUDE_VARIABLES = ['a', 'a_bnds', 'alev1', 'alevel', 'alevhalf', 'alt40', 'b', 'b_bnds', 'bnds',
                             'bounds_lat', 'bounds_lon', 'dbze', 'depth', 'depth0m', 'depth100m', 'depth_bnds',
                             'geo_region', 'height', 'height10m', 'height2m', 'lat', 'lat_bnds', 'latitude',
                             'latitude_bnds', 'layer', 'lev', 'lev_bnds', 'location', 'lon', 'lon_bnds', 'longitude',
                             'longitude_bnds', 'olayer100m', 'olevel', 'oline', 'p0', 'p220', 'p500', 'p560', 'p700',
                             'p840', 'plev', 'plev3', 'plev7', 'plev8', 'plev_bnds', 'plevs', 'pressure1', 'region',
                             'rho', 'scatratio', 'sdepth', 'sdepth1', 'sza5', 'tau', 'tau_bnds', 'time', 'time1',
                             'time2', 'time_bnds', 'vegtype']

VARIABLES_ID = ['a', 'a_bnds', 'abs550aer', 'acabf', 'acabfIs', 'aerasymbnd', 'aeroptbnd', 'aerssabnd', 'agesno', 'agessc', 'a_half', 'a_half_bnds', 'airmass', 'albc', 'albdiffbnd', 'albdirbnd', 'albisccp', 'albsn', 'alt16', 'alt40', 'alternate_hybrid_sigma', 'alternate_hybrid_sigma_half', 'aoanh', 'aod550volso4', 'ap', 'ap_bnds', 'ap_half', 'ap_half_bnds', 'arag', 'aragos', 'areacella', 'areacellg', 'areacello', 'areacellr', 'ares', 'axis_entry', 'b', 'b1', 'b1_half', 'b2', 'b2_half', 'bacc', 'baccos', 'baresoilFrac', 'basin', 'b_bnds', 'bddtalk', 'bddtdic', 'bddtdife', 'bddtdin', 'bddtdip', 'bddtdisi', 'bfe', 'bfeos', 'b_half', 'b_half_bnds', 'bigthetao', 'bigthetaoga', 'bldep', 'bry', 'bs550aer', 'bsi', 'bsios', 'burntFractionAll', 'c13Land', 'c13Litter', 'c13Soil', 'c13Veg', 'c14Land', 'c14Litter', 'c14Soil', 'c14Veg', 'c2h2', 'c2h6', 'c3h6', 'c3h8', 'c3PftFrac', 'c4PftFrac', 'calc', 'calcos', 'ccb', 'ccldncl', 'ccn', 'cct', 'cCwd', 'cdnc', 'cfadDbze94', 'cfadLidarsr532', 'cfc11', 'cfc113global', 'cfc11global', 'cfc12', 'cfc12global', 'ch3coch3', 'ch4', 'ch4Clim', 'ch4global', 'ch4globalClim', 'cheaqpso4', 'chegpso4', 'chepasoa', 'chepsoa', 'chl', 'chlcalc', 'chlcalcos', 'chldiat', 'chldiatos', 'chldiaz', 'chldiazos', 'chlmisc', 'chlmiscos', 'chlos', 'chlpico', 'chlpicoos', 'ci', 'cl', 'cLand', 'clayfrac', 'clc', 'clcalipso', 'clcalipso2', 'clcalipsoice', 'clcalipsoliq', 'cldicemxrat27', 'cldnci', 'cldncl', 'cldnvi', 'cldwatmxrat27', 'cLeaf', 'clhcalipso', 'cli', 'clic', 'climodis', 'clis', 'clisccp', 'cLitter', 'cLitterAbove', 'cLitterBelow', 'cLitterCwd', 'cLitterGrass', 'cLitterLut', 'cLitterShrub', 'cLitterSubSurf', 'cLitterSurf', 'cLitterTree', 'clivi', 'clivic', 'cllcalipso', 'clmcalipso', 'clmisr', 'cls', 'clt', 'cltc', 'cltcalipso', 'cltisccp', 'cltmodis', 'clw', 'clwc', 'clwmodis', 'clws', 'clwvi', 'clwvic', 'cly', 'cMisc', 'cnc', 'co', 'co2', 'co23D', 'co2Clim', 'co2mass', 'co2massClim', 'co2s', 'co3', 'co3abio', 'co3abioos', 'co3nat', 'co3natos', 'co3os', 'co3satarag', 'co3sataragos', 'co3satcalc', 'co3satcalcos', 'cod', 'columnmassflux', 'conccmcn', 'conccn', 'concdust', 'concnmcn', 'cOther', 'cProduct', 'cProductLut', 'cRoot', 'cropFrac', 'cropFracC3', 'cropFracC4', 'cSoil', 'cSoilAbove1m', 'cSoilFast', 'cSoilGrass', 'cSoilLevels', 'cSoilLut', 'cSoilMedium', 'cSoilPools', 'cSoilShrub', 'cSoilSlow', 'cSoilTree', 'cStem', 'cTotFireLut', 'cVeg', 'cVegGrass', 'cVegLut', 'cVegShrub', 'cVegTree', 'cw', 'cWood', 'darag', 'dbze', 'dcalc', 'dcw', 'demc', 'dems', 'depdust', 'depth', 'depth0m', 'depth100m', 'depth2000m', 'depth300m', 'depth700m', 'depth_c', 'depth_coord', 'deptho', 'detoc', 'detocos', 'dfe', 'dfeos', 'dgw', 'diabdrag', 'difmxybo', 'difmxybo2d', 'difmxylo', 'difmxylo2d', 'diftrbbo', 'diftrbbo2d', 'diftrblo', 'diftrblo2d', 'diftrebo', 'diftrebo2d', 'diftrelo', 'diftrelo2d', 'diftrxybo', 'diftrxybo2d', 'diftrxylo', 'diftrxylo2d', 'difvho', 'difvmbo', 'difvmfdo', 'difvmo', 'difvmto', 'difvso', 'difvtrbo', 'difvtrto', 'dispkevfo', 'dispkexyfo', 'dispkexyfo2d', 'dissi13c', 'dissi13cos', 'dissi14c', 'dissi14cabio', 'dissi14cabioos', 'dissic', 'dissicabio', 'dissicabioos', 'dissicnat', 'dissicnatos', 'dissicos', 'dissoc', 'dissocos', 'dmc', 'dmlt', 'dms', 'dmso', 'dmsos', 'dpco2', 'dpco2abio', 'dpco2nat', 'dpo2', 'drivw', 'drybc', 'drydust', 'drynh3', 'drynh4', 'drynoy', 'dryo3', 'dryoa', 'dryso2', 'dryso4', 'dryss', 'dslw', 'dsn', 'dsw', 'dtauc', 'dtaus', 'dtes', 'dtesn', 'ec', 'ec550aer', 'edt', 'effectRadIc', 'effectRadLi', 'emiaco', 'emianox', 'emiaoa', 'emibc', 'emibvoc', 'emico', 'emidms', 'emidust', 'emiisop', 'emilnox', 'eminh3', 'eminox', 'emioa', 'emiso2', 'emiso4', 'emiss', 'emivoc', 'eow', 'eparag100', 'epc100', 'epcalc100', 'epfe100', 'epfy', 'epfz', 'epn100', 'epp100', 'epsi100', 'es', 'esn', 'eta', 'eta2', 'evs', 'evspsbl', 'evspsblpot', 'evspsblsoi', 'evspsblveg', 'evu', 'exparag', 'expc', 'expcalc', 'expfe', 'expn', 'expp', 'expsi', 'fahLut', 'fAnthDisturb', 'fbddtalk', 'fbddtdic', 'fbddtdife', 'fbddtdin', 'fbddtdip', 'fbddtdisi', 'fBNF', 'fCLandToOcean', 'fco2antt', 'fco2fos', 'fco2nat', 'fddtalk', 'fddtdic', 'fddtdife', 'fddtdin', 'fddtdip', 'fddtdisi', 'fDeforestToAtmos', 'fDeforestToProduct', 'fediss', 'fescav', 'fFire', 'fFireAll', 'fFireNat', 'fg13co2', 'fg14co2', 'fg14co2abio', 'fgcfc11', 'fgcfc12', 'fgco2', 'fgco2abio', 'fgco2nat', 'fgdms', 'fgo2', 'fGrazing', 'fgsf6', 'fHarvest', 'fHarvestToAtmos', 'fHarvestToProduct', 'ficeberg', 'ficeberg2d', 'flandice', 'flashrate', 'fldcapacity', 'fLitterFire', 'fLitterSoil', 'fLuc', 'fLulccAtmLut', 'fLulccProductLut', 'fLulccResidueLut', 'fN2O', 'fNAnthDisturb', 'fNdep', 'fNfert', 'fNgas', 'fNgasFire', 'fNgasNonFire', 'fNLandToOcean', 'fNleach', 'fNLitterSoil', 'fNloss', 'fNnetmin', 'fNOx', 'fNProduct', 'fNup', 'fNVegLitter', 'fNVegSoil', 'formula_entry', 'fProductDecomp', 'fProductDecompLut', 'fracInLut', 'fracLut', 'fracOutLut', 'frfe', 'fric', 'friver', 'frn', 'froc', 'fsfe', 'fsitherm', 'fsn', 'fVegFire', 'fVegLitter', 'fVegLitterMortality', 'fVegLitterSenescence', 'fVegSoil', 'fVegSoilMortality', 'fVegSoilSenescence', 'gpp', 'gppc13', 'gppc14', 'gppGrass', 'gppLut', 'gppShrub', 'gppTree', 'grassFrac', 'grassFracC3', 'grassFracC4', 'graz', 'grid_latitude', 'gridlatitude', 'grid_longitude', 'grpllsprof', 'grplmxrat27', 'h2o', 'hcfc22global', 'hcho', 'hcl', 'height100m', 'height10m', 'height2m', 'hfbasin', 'hfbasinpadv', 'hfbasinpmadv', 'hfbasinpmdiff', 'hfbasinpsmadv', 'hfcorr', 'hfds', 'hfdsl', 'hfdsn', 'hfdsnb', 'hfevapds', 'hfgeou', 'hfgeoubed', 'hfibthermds', 'hfibthermds2d', 'hfls', 'hflsIs', 'hflsLut', 'hflso', 'hfmlt', 'hfrainds', 'hfrs', 'hfrunoffds', 'hfrunoffds2d', 'hfsbl', 'hfsifrazil', 'hfsifrazil2d', 'hfsnthermds', 'hfsnthermds2d', 'hfss', 'hfssIs', 'hfssLut', 'hfsso', 'hfx', 'hfy', 'hno3', 'ho2', 'href', 'htovgyre', 'htovovrt', 'hur', 'hurs', 'hursmax', 'hursmin', 'hursminCrop', 'hus', 'hus27', 'hus4', 'hus7h', 'hus850', 'huss', 'hussLut', 'hybrid_height', 'hybrid_height_half', 'iareafl', 'iareagr', 'iceband', 'icem', 'icemIs', 'icfriver', 'i_index', 'intdic', 'intdoc', 'intparag', 'intpbfe', 'intpbn', 'intpbp', 'intpbsi', 'intpcalcite', 'intpn2', 'intpoc', 'intpp', 'intppcalc', 'intppdiat', 'intppdiaz', 'intppmisc', 'intppnitrate', 'intpppico', 'intuadse', 'intuaw', 'intvadse', 'intvaw', 'irrLut', 'isop', 'j_index', 'jno2', 'jo2', 'jo3', 'jpdftaureicemodis', 'jpdftaureliqmodis', 'k_c', 'k_index', 'ksat', 'lai', 'laiLut', 'lambda550nm', 'landCoverFrac', 'landUse', 'latitude', 'libmassbffl', 'libmassbfgr', 'licalvf', 'lifmassbf', 'lim', 'limfecalc', 'limfediat', 'limfediaz', 'limfemisc', 'limfepico', 'limirrcalc', 'limirrdiat', 'limirrdiaz', 'limirrmisc', 'limirrpico', 'limncalc', 'limndiat', 'limndiaz', 'limnmisc', 'limnpico', 'limnsw', 'l_index', 'litempbotfl', 'litempbotgr', 'litemptop', 'litemptopIs', 'lithk', 'loadbc', 'loaddust', 'loadnh4', 'loadno3', 'loadoa', 'loadpoa', 'loadso4', 'loadsoa', 'loadss', 'location', 'longitude', 'lossch4', 'lossco', 'lossn2o', 'lwp', 'lwsffluxaero', 'lwsnl', 'lwsrfasdust', 'lwsrfcsdust', 'lwtoaasdust', 'lwtoacsaer', 'lwtoacsdust', 'lwtoafluxaerocs', 'mapping_entry', 'masscello', 'masso', 'maxpblz', 'mc', 'mcd', 'mcu', 'md', 'meanage', 'mfo', 'm_index', 'minpblz', 'mlotst', 'mlotstmax', 'mlotstmin', 'mlotstsq', 'mmraerh2o', 'mmrbc', 'mmrdust', 'mmrnh4', 'mmrno3', 'mmroa', 'mmrpm1', 'mmrpm10', 'mmrpm2p5', 'mmrso4', 'mmrsoa', 'mmrss', 'modelCellAreai', 'mrfso', 'mrfsofr', 'mrlqso', 'mrlso', 'mrro', 'mrrob', 'mrroIs', 'mrroLi', 'mrroLut', 'mrros', 'mrsfl', 'mrsll', 'mrso', 'mrsofc', 'mrsol', 'mrsoLut', 'mrsos', 'mrsosLut', 'mrsow', 'mrtws', 'msftbarot', 'msftmrho', 'msftmrhompa', 'msftmz', 'msftmzmpa', 'msftmzsmpa', 'msftyrho', 'msftyrhompa', 'msftyz', 'msftyzmpa', 'msftyzsmpa', 'n2o', 'n2oClim', 'n2oglobal', 'n2oglobalClim', 'natural_log_pressure', 'natural_log_pressure_half', 'nbp', 'necbLut', 'nep', 'netAtmosLandC13Flux', 'netAtmosLandC14Flux', 'netAtmosLandCO2Flux', 'nh4', 'nh4os', 'nh50', 'nLand', 'nLeaf', 'nLitter', 'nLitterCwd', 'nLitterSubSurf', 'nLitterSurf', 'nMineral', 'nMineralNH4', 'nMineralNO3', 'no', 'no2', 'no3', 'no3os', 'nOther', 'noy', 'npp', 'nppGrass', 'nppLeaf', 'nppLut', 'nppOther', 'nppRoot', 'nppShrub', 'nppStem', 'nppTree', 'nppWood', 'nProduct', 'nRoot', 'nsigma', 'nSoil', 'nStem', 'nudgincsm', 'nudgincswe', 'nVeg', 'nwdFracLut', 'O18wv', 'o2', 'o2min', 'o2os', 'o2sat', 'o2satos', 'o3', 'o3Clim', 'o3loss', 'o3prod', 'o3ste', 'obvfsq', 'ocean_double_sigma', 'ocean_s', 'ocean_sigma', 'ocean_sigma_z', 'ocfriver', 'ocontempdiff', 'ocontempmint', 'ocontemppadvect', 'ocontemppmdiff', 'ocontemppsmadvect', 'ocontemprmadvect', 'ocontemptend', 'od440aer', 'od443dust', 'od550aer', 'od550aerh2o', 'od550aerso', 'od550bb', 'od550bc', 'od550csaer', 'od550dust', 'od550lt1aer', 'od550no3', 'od550oa', 'od550so4', 'od550so4so', 'od550soa', 'od550ss', 'od865dust', 'od870aer', 'oh', 'olayer100m', 'olevhalf', 'oline', 'omldamax', 'opottempdiff', 'opottempmint', 'opottemppadvect', 'opottemppmdiff', 'opottemppsmadvect', 'opottemprmadvect', 'opottemptend', 'orog', 'orogIs', 'osaltdiff', 'osaltpadvect', 'osaltpmdiff', 'osaltpsmadvect', 'osaltrmadvect', 'osalttend', 'oxloss', 'oxprod', 'p0', 'p10', 'p100', 'p1000', 'p200', 'p220', 'p500', 'p560', 'p700', 'p840', 'p850', 'pabigthetao', 'pan', 'parag', 'parasolRefl', 'pastureFrac', 'pastureFracC3', 'pastureFracC4', 'pathetao', 'pbfe', 'pbo', 'pbsi', 'pcalc', 'pctisccp', 'pflw', 'pfull', 'ph', 'phabio', 'phabioos', 'phalf', 'phnat', 'phnatos', 'phos', 'photo1d', 'phyc', 'phycalc', 'phycalcos', 'phycos', 'phydiat', 'phydiatos', 'phydiaz', 'phydiazos', 'phyfe', 'phyfeos', 'phymisc', 'phymiscos', 'phyn', 'phynos', 'phyp', 'phypico', 'phypicoos', 'phypos', 'physi', 'physios', 'pl700', 'plev19', 'plev23', 'plev27', 'plev3', 'plev39', 'plev3h', 'plev4', 'plev7', 'plev7c', 'plev7h', 'plev8', 'pnitrate', 'po4', 'po4os', 'pod0', 'pon', 'ponos', 'pop', 'popos', 'pp', 'ppcalc', 'ppdiat', 'ppdiaz', 'ppmisc', 'ppos', 'pppico', 'pr', 'pr17O', 'pr18O', 'pr2h', 'prbigthetao', 'prc', 'prcprof', 'prCrop', 'prcsh', 'prhmax', 'prlsns', 'prlsprof', 'prra', 'prraIs', 'prrc', 'prrsn', 'prsn', 'prsn17O', 'prsn18O', 'prsn2h', 'prsnc', 'prsnIs', 'prsnsn', 'prthetao', 'prveg', 'prw', 'prw17O', 'prw18O', 'prw2H', 'ps', 'ps1', 'ps2', 'psitem', 'psl', 'pso', 'ptop', 'ptp', 'qgwr', 'ra', 'rac13', 'rac14', 'raGrass', 'rainmxrat27', 'raLeaf', 'raLut', 'raOther', 'raRoot', 'raShrub', 'raStem', 'raTree', 'reffcclwtop', 'reffclic', 'reffclis', 'reffclwc', 'reffclws', 'reffclwtop', 'reffgrpls', 'reffrainc', 'reffrains', 'reffsclwtop', 'reffsnowc', 'reffsnows', 'remoc', 'residualFrac', 'rGrowth', 'rh', 'rhc13', 'rhc14', 'rhGrass', 'rhLitter', 'rhLut', 'rho', 'rhShrub', 'rhSoil', 'rhTree', 'rivi', 'rivo', 'rld', 'rld4co2', 'rldcs', 'rldcs4co2', 'rlds', 'rldscs', 'rldsIs', 'rlntds', 'rls', 'rlu', 'rlu4co2', 'rlucs', 'rlucs4co2', 'rlus', 'rlusIs', 'rlusLut', 'rlut', 'rlut4co2', 'rlutaf', 'rlutcs', 'rlutcs4co2', 'rlutcsaf', 'rMaint', 'rootd', 'rootdsl', 'rsd', 'rsd4co2', 'rsdcs', 'rsdcs4co2', 'rsdcsaf', 'rsdcsafbnd', 'rsdcsbnd', 'rsdo', 'rsdoabsorb', 'rsds', 'rsdscs', 'rsdscsaf', 'rsdscsafbnd', 'rsdscsbnd', 'rsdscsdiff', 'rsdsdiff', 'rsdsIs', 'rsdt', 'rsntds', 'rss', 'rsu', 'rsu4co2', 'rsucs', 'rsucs4co2', 'rsucsaf', 'rsucsafbnd', 'rsucsbnd', 'rsus', 'rsuscs', 'rsuscsaf', 'rsuscsafbnd', 'rsuscsbnd', 'rsusIs', 'rsusLut', 'rsut', 'rsut4co2', 'rsutaf', 'rsutcs', 'rsutcs4co2', 'rsutcsaf', 'rsutcsafbnd', 'rsutcsbnd', 'rtmt', 'rv850', 'rzwc', 'sample_user_mapping', 'sandfrac', 'sbl', 'sblIs', 'sblnosn', 'scatratio', 'scatter180', 'sci', 'scldncl', 'sconcdust', 'sconcso4', 'sconcss', 'sdepth', 'sdepth1', 'sdepth10', 'sedustCI', 'sf6', 'sfcWind', 'sfcWindmax', 'sfdsi', 'sfno2', 'sfo3', 'sfo3max', 'sfpm25', 'sfriver', 'sftflf', 'sftgif', 'sftgrf', 'sftlf', 'sftof', 'shrubFrac', 'si', 'siage', 'siareaacrossline', 'siarean', 'siareas', 'sicompstren', 'siconc', 'siconca', 'sidconcdyn', 'sidconcth', 'sidivvel', 'sidmassdyn', 'sidmassevapsubl', 'sidmassgrowthbot', 'sidmassgrowthwat', 'sidmasslat', 'sidmassmeltbot', 'sidmassmelttop', 'sidmasssi', 'sidmassth', 'sidmasstranx', 'sidmasstrany', 'sidragbot', 'sidragtop', 'siextentn', 'siextents', 'sifb', 'siflcondbot', 'siflcondtop', 'siflfwbot', 'siflfwdrain', 'sifllatstop', 'sifllwdtop', 'sifllwutop', 'siflsenstop', 'siflsensupbot', 'siflswdbot', 'siflswdtop', 'siflswutop', 'siforcecoriolx', 'siforcecorioly', 'siforceintstrx', 'siforceintstry', 'siforcetiltx', 'siforcetilty', 'sigma', 'sigma_bnds', 'sihc', 'siitdconc', 'siitdsnconc', 'siitdsnthick', 'siitdthick', 'siline', 'siltfrac', 'simass', 'simassacrossline', 'simpconc', 'simpmass', 'simprefrozen', 'sios', 'sipr', 'sirdgconc', 'sirdgthick', 'sisali', 'sisaltmass', 'sishevel', 'sisnconc', 'sisnhc', 'sisnmass', 'sisnthick', 'sispeed', 'sistremax', 'sistresave', 'sistrxdtop', 'sistrxubot', 'sistrydtop', 'sistryubot', 'site', 'sitempbot', 'sitempsnic', 'sitemptop', 'sithick', 'sithreshold', 'sitimefrac', 'siu', 'siv', 'sivol', 'sivoln', 'sivols', 'sltbasin', 'slthick', 'sltovgyre', 'sltovovrt', 'smc', 'smooth_level', 'smooth_level_half', 'snc', 'sncIs', 'snd', 'sndmassdyn', 'sndmassmelt', 'sndmasssi', 'sndmasssnf', 'sndmasssubl', 'sndmasswindrif', 'snicefreez', 'snicefreezIs', 'snicem', 'snicemIs', 'snm', 'snmassacrossline', 'snmIs', 'snmsl', 'snowband', 'snowmxrat27', 'snrefr', 'snw', 'snwc', 'so', 'so2', 'sob', 'soga', 'soilpools', 'solbnd', 'somint', 'sootsn', 'sos', 'sosga', 'sossq', 'spco2', 'spco2abio', 'spco2nat', 'spectband', 'standard_hybrid_sigma', 'standard_hybrid_sigma_half', 'standard_sigma', 'standard_sigma_half', 'stempzero', 'strbasemag', 'sw', 'sw18O', 'sw2H', 'sweLut', 'swsffluxaero', 'swsrfasdust', 'swsrfcsdust', 'swtoaasdust', 'swtoacsdust', 'swtoafluxaerocs', 'sza', 'sza5', 't2', 't20d', 'ta', 'ta27', 'ta500', 'ta700', 'ta7h', 'ta850', 'talk', 'talknat', 'talknatos', 'talkos', 'tas', 'tasIs', 'tasLut', 'tasmax', 'tasmaxCrop', 'tasmin', 'tasminCrop', 'tatp', 'tau', 'tauu', 'tauucorr', 'tauuo', 'tauupbl', 'tauv', 'tauvcorr', 'tauvo', 'tauvpbl', 'tcs', 'tdps', 'tendacabf', 'tendlibmassbf', 'tendlicalvf', 'tgs', 'thetao', 'thetaoga', 'thetaot', 'thetaot2000', 'thetaot300', 'thetaot700', 'thkcello', 'time', 'time1', 'time2', 'time3', 'tnhus', 'tnhusa', 'tnhusc', 'tnhusd', 'tnhusmp', 'tnhuspbl', 'tnhusscp', 'tnhusscpbl', 'tnkebto', 'tnkebto2d', 'tnpeo', 'tnpeot', 'tnpeotb', 'tnt', 'tnta', 'tntc', 'tntd', 'tntmp', 'tntmp27', 'tntnogw', 'tntogw', 'tntpbl', 'tntr', 'tntr27', 'tntrl', 'tntrl27', 'tntrlcs', 'tntrs', 'tntrs27', 'tntrscs', 'tntscp', 'tntscpbl', 'tob', 'topg', 'tos', 'tosga', 'tossq', 'toz', 'tpf', 'tr', 'tran', 'treeFrac', 'treeFracBdlDcd', 'treeFracBdlEvg', 'treeFracNdlDcd', 'treeFracNdlEvg', 'treeFracPrimDec', 'treeFracPrimEver', 'treeFracSecDec', 'treeFracSecEver', 'tropoz', 'ts', 'tsIs', 'tsl', 'tsland', 'tslsi', 'tslsiLut', 'tsn', 'tsnIs', 'tsns', 'tSoilPools', 'ttop', 'twap', 'typebare', 'typeburnt', 'typec3crop', 'typec3natg', 'typec3pastures', 'typec3pft', 'typec4crop', 'typec4natg', 'typec4pastures', 'typec4pft', 'typecloud', 'typecrop', 'typefis', 'typegis', 'typeland', 'typeli', 'typemp', 'typenatgr', 'typenwd', 'typepasture', 'typepdec', 'typepever', 'typeresidual', 'typesdec', 'typesea', 'typesever', 'typeshrub', 'typesi', 'typesirdg', 'typetree', 'typetreebd', 'typetreebe', 'typetreend', 'typetreene', 'typeveg', 'typewetla', 'u2', 'ua', 'ua10', 'ua100m', 'ua27', 'ua7h', 'uas', 'ugrid', 'umo', 'uo', 'uqint', 'ut', 'utendepfd', 'utendnogw', 'utendnogw27', 'utendogw', 'utendvtem', 'utendwtem', 'uv', 'uwap', 'v2', 'va', 'va100m', 'va27', 'va7h', 'vas', 'vegFrac', 'vegHeight', 'vegHeightCrop', 'vegHeightGrass', 'vegHeightPasture', 'vegHeightShrub', 'vegHeightTree', 'vegtype', 'vertices', 'vertices_latitude', 'vertices_longitude', 'vmo', 'vmrox', 'vo', 'volcello', 'volo', 'vortmean', 'vqint', 'vsf', 'vsfcorr', 'vsfevap', 'vsfpr', 'vsfriver', 'vsfsit', 'vt', 'vt100', 'vtem', 'vtendnogw', 'vtendnogw27', 'vtendogw', 'vwap', 'wa', 'wap', 'wap2', 'wap27', 'wap4', 'wap500', 'wap7h', 'wbptemp7h', 'wetbc', 'wetdust', 'wetlandCH4', 'wetlandCH4cons', 'wetlandCH4prod', 'wetlandFrac', 'wetnh3', 'wetnh4', 'wetnoy', 'wetoa', 'wetso2', 'wetso4', 'wetss', 'wfcorr', 'wfo', 'wfonocorr', 'wilt', 'wmo', 'wo', 'wsgmax100m', 'wsgmax10m', 'wtd', 'wtem', 'x', 'xant', 'x_deg', 'xgre', 'xgwdparam', 'xvelbase', 'xvelmean', 'xvelsurf', 'y', 'yant', 'y_deg', 'ygre', 'ygwdparam', 'yvelbase', 'yvelmean', 'yvelsurf', 'z1', 'z2', 'zfull', 'zfullo', 'zg', 'zg10', 'zg100', 'zg1000', 'zg27', 'zg500', 'zg7h', 'zhalf', 'zhalfo', 'zlev', 'zlev_bnds', 'zmeso', 'zmesoos', 'zmicro', 'zmicroos', 'zmisc', 'zmiscos', 'zmla', 'zmlwaero', 'zmswaero', 'zmtnt', 'zo2min', 'zooc', 'zoocos', 'zos', 'zossq', 'zostoga', 'zsatarag', 'zsatcalc', 'ztop', 'ztp', 'zvelbase', 'zvelsurf']

# netCDF global attribute delimiter
ATTRIBUTE_DELIMITERS = {'realm': 'space', 'activity_id': 'space', 'source_type': 'space', 'model_cohort': 'space'}  # use the facet name

# Handler
HANDLER = 'esgcet.config.cmip6_handler:CMIP6Handler'

# MIP Era value
MIP_ERA = 'CMIP6'

# Oldest CMOR version allowed
MIN_CMOR_VERSION = '3.2.4'

# Oldest Data Specs version allowed

MIN_DS_VERSION = '01.00.13'

# Oldest CF version allowed
MIN_CF_VERSION = '1.6'

# CIM docs creation boolean
CREATE_CIM = 'true'

# LAS configuration boolean
LAS_CONFIGURE = 'true'

