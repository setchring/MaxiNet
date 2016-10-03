from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        CHE = self.addSwitch('CHE0')
        LEI = self.addSwitch('LEI0')
        ADH = self.addSwitch('ADH0')
        DRE = self.addSwitch('DRE0')
        GSI = self.addSwitch('GSI0')
        HEI = self.addSwitch('HEI0')
        JEN = self.addSwitch('JEN0')
        ILM = self.addSwitch('ILM0')
        DeCix = self.addSwitch('DeCix0')
        Geant = self.addSwitch('Geant0')
        FZK = self.addSwitch('FZK0')
        STU = self.addSwitch('STU0')
        DeCix = self.addSwitch('DeCix0')
        Telia = self.addSwitch('Telia0')
        BIE = self.addSwitch('BIE0')
        Telekom = self.addSwitch('Telekom0')
        GOE = self.addSwitch('GOE0')
        BRE = self.addSwitch('BRE0')
        WUP = self.addSwitch('WUP0')
        BIR = self.addSwitch('BIR0')
        BON = self.addSwitch('BON0')
        MAR = self.addSwitch('MAR0')
        GIE = self.addSwitch('GIE0')
        KAS = self.addSwitch('KAS0')
        PAD = self.addSwitch('PAD0')
        EWE = self.addSwitch('EWE0')
        Telekom = self.addSwitch('Telekom0')
        MUE = self.addSwitch('MUE0')
        SAA = self.addSwitch('SAA0')
        GC = self.addSwitch('GC0')
        DES = self.addSwitch('DES0')
        HAM = self.addSwitch('HAM0')
        KIE = self.addSwitch('KIE0')
        ROS = self.addSwitch('ROS0')
        MAG = self.addSwitch('MAG0')
        BRA = self.addSwitch('BRA0')
        KAI = self.addSwitch('KAI0')
        GRE = self.addSwitch('GRE0')
        DOR = self.addSwitch('DOR0')
        BOC = self.addSwitch('BOC0')
        FHM = self.addSwitch('FHM0')
        REG = self.addSwitch('REG0')
        AUG = self.addSwitch('AUG0')
        GAR = self.addSwitch('GAR0')
        DUI = self.addSwitch('DUI0')
        FZJ = self.addSwitch('FZJ0')
        AAC = self.addSwitch('AAC0')
        WUE = self.addSwitch('WUE0')
        TUB = self.addSwitch('TUB0')
        HUB = self.addSwitch('HUB0')
        HAN = self.addSwitch('HAN0')
        FRA = self.addSwitch('FRA0')
        POT = self.addSwitch('POT0')
        ERL = self.addSwitch('ERL0')
        BAY = self.addSwitch('BAY0')
        FFO = self.addSwitch('FFO0')
        ZIB = self.addSwitch('ZIB0')
        ZEU = self.addSwitch('ZEU0')
        # Add links
        self.addLink(CHE, LEI)
        self.addLink(CHE, DRE)
        self.addLink(LEI, ERL)
        self.addLink(LEI, JEN)
        self.addLink(LEI, Telekom)
        self.addLink(ADH, ZIB)
        self.addLink(ADH, HUB)
        self.addLink(DRE, POT)
        self.addLink(DRE, ERL)
        self.addLink(GSI, FRA)
        self.addLink(GSI, HEI)
        self.addLink(HEI, FZK)
        self.addLink(JEN, ILM)
        self.addLink(ILM, ERL)
        self.addLink(DeCix, FRA)
        self.addLink(Geant, FRA)
        self.addLink(FZK, STU)
        self.addLink(FZK, FRA)
        self.addLink(FZK, KAI)
        self.addLink(STU, GAR)
        self.addLink(DeCix, POT)
        self.addLink(Telia, POT)
        self.addLink(BIE, PAD)
        self.addLink(BIE, HAN)
        self.addLink(BIE, MUE)
        self.addLink(GOE, HAN)
        self.addLink(GOE, KAS)
        self.addLink(BRE, EWE)
        self.addLink(BRE, HAN)
        self.addLink(BRE, HAM)
        self.addLink(WUP, BIR)
        self.addLink(WUP, DOR)
        self.addLink(BIR, FRA)
        self.addLink(BIR, BON)
        self.addLink(BON, AAC)
        self.addLink(MAR, GIE)
        self.addLink(MAR, KAS)
        self.addLink(GIE, FRA)
        self.addLink(KAS, PAD)
        self.addLink(EWE, MUE)
        self.addLink(Telekom, HAN)
        self.addLink(MUE, DUI)
        self.addLink(SAA, FRA)
        self.addLink(SAA, KAI)
        self.addLink(GC, FRA)
        self.addLink(DES, TUB)
        self.addLink(DES, HAM)
        self.addLink(KIE, ROS)
        self.addLink(KIE, HAN)
        self.addLink(ROS, HAN)
        self.addLink(ROS, GRE)
        self.addLink(MAG, BRA)
        self.addLink(MAG, POT)
        self.addLink(BRA, HAN)
        self.addLink(KAI, FRA)
        self.addLink(GRE, POT)
        self.addLink(DOR, BOC)
        self.addLink(BOC, DUI)
        self.addLink(FHM, REG)
        self.addLink(FHM, GAR)
        self.addLink(REG, ERL)
        self.addLink(AUG, GAR)
        self.addLink(AUG, ERL)
        self.addLink(GAR, FRA)
        self.addLink(DUI, HAN)
        self.addLink(DUI, FZJ)
        self.addLink(FZJ, AAC)
        self.addLink(AAC, FRA)
        self.addLink(WUE, FRA)
        self.addLink(WUE, ERL)
        self.addLink(TUB, ZIB)
        self.addLink(TUB, HUB)
        self.addLink(TUB, POT)
        self.addLink(TUB, ZEU)
        self.addLink(HAN, FRA)
        self.addLink(HAN, POT)
        self.addLink(HAN, ERL)
        self.addLink(HAN, FFO)
        self.addLink(FRA, POT)
        self.addLink(FRA, ERL)
        self.addLink(POT, ERL)
        self.addLink(POT, BAY)
        self.addLink(POT, FFO)
        self.addLink(POT, ZIB)
        self.addLink(ERL, BAY)
        self.addLink(FFO, ZIB)
        self.addLink(ZIB, ZEU)
topos = { 'mytopo': ( lambda: MyTopo() ) }