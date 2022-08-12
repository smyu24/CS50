import random

def color_pick():
    picker = random.randint(1, 11)
    if picker == 1:
        #Group #1
        """
        COLOR 1:
        R: 245
        G: 238
        B: 194

        COLOR 2:
        R: 65
        G: 106
        B: 89

        COLOR 3:
        R: 57
        G: 57
        B: 95

        COLOR 4:
        R: 115
        G: 162
        B: 78

        COLOR 5:
        R: 169
        G: 194
        B: 93
        """
        return [(245,238,194),(65,106,89),(57,57,95),(115,162,78),(169,194,93)]
    elif picker == 2:
        #Group #2
        """
        COLOR 1:
        R: 246
        G: 196
        B: 83

        COLOR 2:
        R: 254
        G: 251
        B: 233

        COLOR 3:
        R: 240
        G: 160
        B: 75

        COLOR 4:
        R: 24
        G: 58
        B: 29

        COLOR 5:
        R: 255
        G: 238
        B: 221
        """
        return [(246,196,83),(254,251,233),(240,160,75),(24,58,29),(255,238,221)]

    elif picker == 3:
        #Group #3
        """
        COLOR 1:
        R: 228
        G: 221
        B: 244

        COLOR 2:
        R: 148
        G: 61
        B: 38

        COLOR 3:
        R: 255
        G: 251
        B: 240

        COLOR 4:
        R: 45
        G: 45
        B: 45

        COLOR 5:
        R: 40
        G: 38
        B: 18
        """
        return [(228,221,244),(148,61,38),(255,251,240),(45,45,45),(40,38,18)]

    elif picker == 4:
        #Group #4
        """
        COLOR 1:
        R: 57
        G: 119
        B: 84

        COLOR 2:
        R: 240
        G: 163
        B: 188

        COLOR 3:
        R: 112
        G: 190
        B: 81

        COLOR 4:
        R: 235
        G: 107
        B: 64

        COLOR 5:
        R: 155
        G: 69
        B: 178
        """
        return [(57,119,84),(240,163,188),(112,190,81),(235,107,64),(155,69,178)]

    elif picker == 5:
        #Group #5
        """
        COLOR 1:
        R: 91
        G: 204
        B: 246

        COLOR 2:
        R: 252
        G: 222
        B: 103

        COLOR 3:
        R: 3
        G: 14
        B: 18
        """
        return [(91,204,246),(252,222,103),(3,14,18)]

    elif picker == 6:
        #Group #6
        """
        COLOR 1:
        R: 239
        G: 146
        B: 115

        COLOR 2:
        R: 254
        G: 249
        B: 248

        COLOR 3:
        R: 13
        G: 13
        B: 13
        """
        return [(239,146,115),(254,249,148),(13,13,13)]


    elif picker == 7:
        #Group #7
        """
        COLOR 1:
        R: 43
        G: 103
        B: 119

        COLOR 2:
        R: 200
        G: 216
        B: 228

        COLOR 3:
        R: 255
        G: 255
        B: 255

        COLOR 4:
        R: 242
        G: 242
        B: 242

        COLOR 5:
        R: 82
        G: 171
        B: 152
        """
        return [(43,103,119),(200,216,228),(255,255,255),(242,242,242),(82,171,152)]

    elif picker == 8:
        #Group #8
        """
        COLOR 1:
        R: 250
        G: 229
        B: 223

        COLOR 2:
        R: 245
        G: 202
        B: 194

        COLOR 3:
        R: 237
        G: 121
        B: 102

        COLOR 4:
        R: 48
        G: 49
        B: 121

        COLOR 5:
        R: 20
        G: 24
        B: 80
        """
        return [(150,229,223),(245,202,194),(237,121,102),(48,49,121),(20,24,80)]

    elif picker == 9:
        #Group #9
        """
        COLOR 1:
        R: 95
        G: 44
        B: 62

        COLOR 2:
        R: 209
        G: 173
        B: 204

        COLOR 3:
        R: 194
        G: 210
        B: 189

        COLOR 4:
        R: 198
        G: 80
        B: 50

        COLOR 5:
        R: 246
        G: 233
        B: 215
        """
        return [(95,44,62),(209,173,204),(194,210,189),(198,80,50),(246,233,215)]

    elif picker == 10:
        #Group #10
        """
        COLOR 1:
        R: 27
        G: 77
        B: 137

        COLOR 2:
        R: 249
        G: 228
        B: 91

        COLOR 3:
        R: 109
        G: 183
        B: 132

        COLOR 4:
        R: 255
        G: 255
        B: 255
        """
        return [(27,77,137),(249,228,91),(109,183,132),(255,255,255)]

    else: #elif picker == 11:
        #Group #11
        """
        COLOR 1:
        R: 237
        G: 220
        B: 217

        COLOR 2:
        R: 242
        G: 235
        B: 233

        COLOR 3:
        R: 222
        G: 84
        B: 153

        COLOR 4:
        R: 38
        G: 65
        B: 67

        COLOR 5:
        R: 233
        G: 159
        B: 76
        """
        return [(237,220,217),(242,235,233),(222,84,153),(38,65,67),(233,159,76)]

    #Group #_
    """
    COLOR 1:
    R:
    G:
    B:

    COLOR 2:
    R:
    G:
    B:

    COLOR 3:
    R:
    G:
    B:

    COLOR 4:
    R:
    G:
    B:

    COLOR 5:
    R:
    G:
    B:
    """