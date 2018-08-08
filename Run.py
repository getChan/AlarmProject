import ScoreBoardPipe, ExtractGameId, MatchData

gameid = ExtractGameId.ExtractGameId()
son = MatchData.IsStarting(gameid)

print("손흥민 선발? "+str(son))