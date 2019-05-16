
class ve_strategy:
    def __init__(self):
        self.vote_parameters = {}
        self.vote_parameters['type'] = 'normal'
        self.vote_parameters['voter'] = 'both'
        self.vote_parameters['height'] = 4
        self.vote_parameters['diff_measure'] = 'abs';
        self.vote_parameters['decision_type'] = 'loose';
        self.vote_parameters['Threshold_T'] = 0
        self.vote_parameters['Threshod_R'] = 0
        self.vote_parameters['Threshold_max'] = 3;