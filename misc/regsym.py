regs="""
;Core registers
IMR                .set 0004h   ;Interrupt mask reg
GREG               .set 0005h   ;Global memory allocation reg
IFR                .set 0006h   ;Interrupt flag reg
;System configuration and interrupt registers
PIRQR0             .set 7010h   ;Peripheral interrupt request reg 0
PIRQR1             .set 7011h   ;Peripheral interrupt request reg 1
PIRQR2             .set 7012h   ;Peripheral interrupt request reg 2 
PIACKR0            .set 7014h   ;Peripheral interrupt acknowledge reg 0
PIACKR1            .set 7015h   ;Peripheral interrupt acknowledge reg 1
PIACKR2            .set 7016h   ;Peripheral interrupt acknowledge reg 2
SCSR1              .set 7018h   ;System control & status reg 1
SCSR2              .set 7019h   ;System control & status reg 2
DINR               .set 701Ch   ;Device identification reg
PIVR               .set 701Eh   ;Peripheral interrupt vector reg

;Watchdog timer (WD) registers
WDCNTR             .set 7023h   ;WD counter reg
WDKEY              .set 7025h   ;WD reset key reg
WDCR               .set 7029h   ;WD timer control reg

;Serial Peripheral Interface (SPI) registers
SPICCR             .set 7040h   ;SPI configuration control reg
SPICTL             .set 7041h   ;SPI operation control reg
SPISTS             .set 7042h   ;SPI status reg
SPIBRR             .set 7044h   ;SPI baud rate reg
SPIRXEMU           .set 7046h   ;SPI emulation buffer reg
SPIRXBUF           .set 7047h   ;SPI serial receive buffer reg
SPITXBUF           .set 7048h   ;SPI serial transmit buffer reg
SPIDAT             .set 7049h   ;SPI serial data reg
SPIPRI             .set 704Fh   ;SPI priority control reg

;SCI registers
SCICCR             .set 7050h   ;SCI communication control reg
SCICTL1            .set 7051h   ;SCI control reg 1
SCIHBAUD           .set 7052h   ;SCI baud-select reg, high bits
SCILBAUD           .set 7053h   ;SCI baud-select reg, low bits
SCICTL2            .set 7054h   ;SCI control reg 2
SCIRXST            .set 7055h   ;SCI receiver status reg
SCIRXEMU           .set 7056h   ;SCI emulation data buffer reg
SCIRXBUF           .set 7057h   ;SCI receiver data buffer reg
SCITXBUF           .set 7059h   ;SCI transmit data buffer reg
SCIPRI             .set 705Fh   ;SCI priority control reg

;External interrupt configuration registers
XINT1CR            .set 7070h   ;Ext interrupt 1 config reg
XINT2CR            .set 7071h   ;Ext interrupt 2 config reg

;Digital I/O registers
MCRA               .set 7090h   ;I/O mux control reg A
MCRB               .set 7092h   ;I/O mux control reg B
MCRC               .set 7094h   ;I/O mux control reg C
PADATDIR           .set 7098h   ;I/O port A data & dir reg
PBDATDIR           .set 709Ah   ;I/O port B data & dir reg
PCDATDIR           .set 709Ch   ;I/O port C data & dir reg
PDDATDIR           .set 709Eh   ;I/O port D data & dir reg
PEDATDIR           .set 7095h   ;I/O port E data & dir reg
PFDATDIR           .set 7096h   ;I/O port F data & dir reg

;Analog-to-Digital Converter (ADC) registers
ADCTRL1            .set 70A0h   ;ADC control reg 1
ADCTRL2            .set 70A1h   ;ADC control reg 2
MAX_CONV           .set 70A2h   ;Maximum conversion channels reg
CHSELSEQ1          .set 70A3h   ;Channel select sequencing control reg 1
CHSELSEQ2          .set 70A4h   ;Channel select sequencing control reg 2
CHSELSEQ3          .set 70A5h   ;Channel select sequencing control reg 3
CHSELSEQ4          .set 70A6h   ;Channel select sequencing control reg 4
AUTO_SEQ_SR        .set 70A7h   ;Autosequence status reg
RESULT0            .set 70A8h   ;Conversion result buffer reg 0
RESULT1            .set 70A9h   ;Conversion result buffer reg 1
RESULT2            .set 70AAh   ;Conversion result buffer reg 2
RESULT3            .set 70ABh   ;Conversion result buffer reg 3
RESULT4            .set 70ACh   ;Conversion result buffer reg 4
RESULT5            .set 70ADh   ;Conversion result buffer reg 5
RESULT6            .set 70AEh   ;Conversion result buffer reg 6
RESULT7            .set 70AFh   ;Conversion result buffer reg 7
RESULT8            .set 70B0h   ;Conversion result buffer reg 8
RESULT9            .set 70B1h   ;Conversion result buffer reg 9
RESULT10           .set 70B2h   ;Conversion result buffer reg 10
RESULT11           .set 70B3h   ;Conversion result buffer reg 11
RESULT12           .set 70B4h   ;Conversion result buffer reg 12
RESULT13           .set 70B5h   ;Conversion result buffer reg 13
RESULT14           .set 70B6h   ;Conversion result buffer reg 14
RESULT15           .set 70B7h   ;Conversion result buffer reg 15
CALIBRATION        .set 70B8h   ;Calibration result reg

;Controller Area Network (CAN) registers
MDER               .set 7100h   ;CAN mailbox direction/enable reg
TCR                .set 7101h   ;CAN transmission control reg
RCR                .set 7102h   ;CAN receive control reg
MCR                .set 7103h   ;CAN master control reg
BCR2               .set 7104h   ;CAN bit config reg 2
BCR1               .set 7105h   ;CAN bit config reg 1
ESR                .set 7106h   ;CAN error status reg
GSR                .set 7107h   ;CAN global status reg
CEC                .set 7108h   ;CAN trans and rcv err counters
CAN_IFR            .set 7109h   ;CAN interrupt flag reg 
CAN_IMR            .set 710ah   ;CAN interrupt mask reg
LAM0_H             .set 710bh   ;CAN local acceptance mask MBX0/1
LAM0_L             .set 710ch   ;CAN local acceptance mask MBX0/1
LAM1_H             .set 710dh   ;CAN local acceptance mask MBX2/3
LAM1_L             .set 710eh   ;CAN local acceptance mask MBX2/3

MSGID0L            .set 7200h   ;CAN message ID for mailbox 0 (lower 16 bits)
MSGID0H            .set 7201h   ;CAN message ID for mailbox 0 (upper 16 bits)
MSGCTRL0           .set 7202h   ;CAN RTR and DLC for mailbox 0
MBX0A              .set 7204h   ;CAN 2 of 8 bytes of mailbox 0
MBX0B              .set 7205h   ;CAN 2 of 8 bytes of mailbox 0
MBX0C              .set 7206h   ;CAN 2 of 8 bytes of mailbox 0
MBX0D              .set 7207h   ;CAN 2 of 8 bytes of mailbox 0

MSGID1L            .set 7208h   ;CAN message ID for mailbox 1 (lower 16 bits)
MSGID1H            .set 7209h   ;CAN message ID for mailbox 1 (upper 16 bits)
MSGCTRL1           .set 720Ah   ;CAN RTR and DLC for mailbox 1
MBX1A              .set 720Ch   ;CAN 2 of 8 bytes of mailbox 1
MBX1B              .set 720Dh   ;CAN 2 of 8 bytes of mailbox 1
MBX1C              .set 720Eh   ;CAN 2 of 8 bytes of mailbox 1
MBX1D              .set 720Fh   ;CAN 2 of 8 bytes of mailbox 1

MSGID2L            .set 7210h   ;CAN message ID for mailbox 2 (lower 16 bits)
MSGID2H            .set 7211h   ;CAN message ID for mailbox 2 (upper 16 bits)
MSGCTRL2           .set 7212h   ;CAN RTR and DLC for mailbox 2
MBX2A              .set 7214h   ;CAN 2 of 8 bytes of mailbox 2
MBX2B              .set 7215h   ;CAN 2 of 8 bytes of mailbox 2
MBX2C              .set 7216h   ;CAN 2 of 8 bytes of mailbox 2
MBX2D              .set 7217h   ;CAN 2 of 8 bytes of mailbox 2

MSGID3L            .set 7218h   ;CAN message ID for mailbox 3 (lower 16 bits)
MSGID3H            .set 7219h   ;CAN message ID for mailbox 3 (upper 16 bits)
MSGCTRL3           .set 721Ah   ;CAN RTR and DLC for mailbox 3
MBX3A              .set 721Ch   ;CAN 2 of 8 bytes of mailbox 3
MBX3B              .set 721Dh   ;CAN 2 of 8 bytes of mailbox 3
MBX3C              .set 721Eh   ;CAN 2 of 8 bytes of mailbox 3
MBX3D              .set 721Fh   ;CAN 2 of 8 bytes of mailbox 3

MSGID4L            .set 7220h   ;CAN message ID for mailbox 4 (lower 16 bits)
MSGID4H            .set 7221h   ;CAN message ID for mailbox 4 (upper 16 bits)
MSGCTRL4           .set 7222h   ;CAN RTR and DLC for mailbox 4
MBX4A              .set 7224h   ;CAN 2 of 8 bytes of mailbox 4
MBX4B              .set 7225h   ;CAN 2 of 8 bytes of mailbox 4
MBX4C              .set 7226h   ;CAN 2 of 8 bytes of mailbox 4
MBX4D              .set 7227h   ;CAN 2 of 8 bytes of mailbox 4

MSGID5L            .set 7228h   ;CAN message ID for mailbox 5 (lower 16 bits)
MSGID5H            .set 7229h   ;CAN message ID for mailbox 5 (upper 16 bits)
MSGCTRL5           .set 722Ah   ;CAN RTR and DLC for mailbox 5
MBX5A              .set 722Ch   ;CAN 2 of 8 bytes of mailbox 5
MBX5B              .set 722Dh   ;CAN 2 of 8 bytes of mailbox 5
MBX5C              .set 722Eh   ;CAN 2 of 8 bytes of mailbox 5
MBX5D              .set 722Fh   ;CAN 2 of 8 bytes of mailbox 5

;Event Manager A (EVA) registers
GPTCONA            .set 7400h   ;GP timer control reg A  
T1CNT              .set 7401h   ;GP timer 1 counter reg 
T1CMPR             .set 7402h   ;GP timer 1 compare reg 
T1PR               .set 7403h   ;GP timer 1 period reg 
T1CON              .set 7404h   ;GP timer 1 control reg 
T2CNT              .set 7405h   ;GP timer 2 counter reg 
T2CMPR             .set 7406h   ;GP timer 2 compare reg 
T2PR               .set 7407h   ;GP timer 2 period reg 
T2CON              .set 7408h   ;GP timer 2 control reg 
COMCONA            .set 7411h   ;Compare control reg A
ACTRA              .set 7413h   ;Compare action control reg A
DBTCONA            .set 7415h   ;Dead-band timer control reg A 
CMPR1              .set 7417h   ;compare reg 1 
CMPR2              .set 7418h   ;compare reg 2 
CMPR3              .set 7419h   ;compare reg 3 
CAPCONA            .set 7420h   ;Capture control reg A 
CAPFIFOA           .set 7422h   ;Capture FIFO status reg A 
CAP1FIFO           .set 7423h   ;Capture Channel 1 FIFO top 
CAP2FIFO           .set 7424h   ;Capture Channel 2 FIFO top 
CAP3FIFO           .set 7425h   ;Capture Channel 3 FIFO top 
CAP1FBOT           .set 7427h   ;Bottom reg of capture FIFO stack 1 
CAP2FBOT           .set 7427h   ;Bottom reg of capture FIFO stack 2 
CAP3FBOT           .set 7427h   ;Bottom reg of capture FIFO stack 3 
EVAIMRA            .set 742Ch   ;EVA interrupt mask reg A
EVAIMRB            .set 742Dh   ;EVA interrupt mask reg B
EVAIMRC            .set 742Eh   ;EVA interrupt mask reg C
EVAIFRA            .set 742Fh   ;EVA interrupt flag reg A
EVAIFRB            .set 7430h   ;EVA interrupt flag reg B
EVAIFRC            .set 7431h   ;EVA interrupt flag reg C

;Event Manager B (EVB) registers
GPTCONB            .set 7500h   ;GP timer control reg B 
T3CNT              .set 7501h   ;GP timer 3 counter reg
T3CMPR             .set 7502h   ;GP timer 3 compare reg
T3PR               .set 7503h   ;GP timer 3 period reg
T3CON              .set 7504h   ;GP timer 3 control reg
T4CNT              .set 7505h   ;GP timer 4 counter reg
T4CMPR             .set 7506h   ;GP timer 4 compare reg
T4PR               .set 7507h   ;GP timer 4 period reg
T4CON              .set 7508h   ;GP timer 4 control reg
COMCONB            .set 7511h   ;Compare control register B
ACTRB              .set 7513h   ;Compare action control register B
DBTCONB            .set 7515h   ;Dead-band timer control reg B
CMPR4              .set 7517h   ;Compare reg 4 
CMPR5              .set 7518h   ;Compare reg 5
CMPR6              .set 7519h   ;Compare reg 6
CAPCONB            .set 7520h   ;Capture control reg B 
CAPFIFOB           .set 7522h   ;Capture FIFO status reg B
CAP4FIFO           .set 7523h   ;Capture channel 4 FIFO top 
CAP5FIFO           .set 7524h   ;Capture channel 5 FIFO top 
CAP6FIFO           .set 7525h   ;Capture channel 6 FIFO top 
CAP4FBOT           .set 7527h   ;Bottom reg of capture FIFO stack 4 
CAP5FBOT           .set 7527h   ;Bottom reg of capture FIFO stack 5 
CAP6FBOT           .set 7527h   ;Bottom reg of capture FIFO stack 6 
EVBIMRA            .set 752Ch   ;EVB interrupt mask reg A
EVBIMRB            .set 752Dh   ;EVB interrupt mask reg B
EVBIMRC            .set 752Eh   ;EVB interrupt mask reg C
EVBIFRA            .set 752Fh   ;EVB interrupt flag reg A
EVBIFRB            .set 7530h   ;EVB interrupt flag reg B
EVBIFRC            .set 7531h   ;EVB interrupt flag reg C
;I/O space mapped registers
FCMR               .set 0FF0Fh  ;Flash control mode reg
WSGR               .set 0FFFFh  ;Wait-state generator reg
"""

for l in regs.split("\n"):

    l = l.strip()
    if not l:
        continue

    if l.startswith(";"):
        print()
        print(f"<!-- {l[1:]} -->")
    else:
        r = l
        for n in range(100):
            r = r.replace("  "," ")
        r = r.split(' ', 3)
        print(f'<symbol name="{r[0]}" address="ram:{r[2][0:4]}" entry="false"/><!-- {r[3][1:]} -->')
