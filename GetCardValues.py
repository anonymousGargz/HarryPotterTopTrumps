class ReturnPlayer1Values():
    def __init__(self):
        pass
    def __GetValueChosenByPlayer1__(self, valueChosen):
        #This matches the button Player1 has clicked on and gets the number displayed on the button 
        #for Player 1 and Player 2,
        # by calling the Return(stat) functions from the PlayPage interface#
        match valueChosen:
                case 'SpellSkillPlayer1':
                    PlayerValues= self.ReturnSpellSkill()
                case 'BraverySkillPlayer1':
                    PlayerValues=self.ReturnBraverySkill()
                case 'BroomSkillPlayer1':
                    PlayerValues=self.ReturnBroomSkill()
                case 'KindnessSkillPlayer1':
                    PlayerValues=self.ReturnKindnessSkill()
                case 'StrengthSkillPlayer1':
                    PlayerValues=self.ReturnStrengthSkill()
                case 'TopTrumpsRatingPlayer1':
                    PlayerValues=self.ReturnTopTrumpsRating()
        return PlayerValues

class ReturnPlayer2Values():
    def __init__(self):
        pass

    def __GetValueChosenByPlayer2__(self, valueChosen):
    #This matches the button Player2 has clicked on and gets the number displayed on the button for 
        #Player 1 and Player 2,
    # by calling the Return(stat) functions from the PlayPage interface#
        match valueChosen:
                case 'SpellSkillPlayer2':
                    PlayerValues= self.ReturnSpellSkill()
                case 'BraverySkillPlayer2':
                    PlayerValues=self.ReturnBraverySkill()
                case 'BroomSkillPlayer2':
                    PlayerValues=self.ReturnBroomSkill()
                case 'KindnessSkillPlayer2':
                    PlayerValues=self.ReturnKindnessSkill()
                case 'StrengthSkillPlayer2':
                    PlayerValues=self.ReturnStrengthSkill()
                case 'TopTrumpsRatingPlayer2':
                    PlayerValues=self.ReturnTopTrumpsRating()
        return PlayerValues

        