from ...core.config_manager import Config


class _BotCommands:
    def __init__(self):
        self.StartCommand = f"start{Config.CMD_SUFFIX}"
        self.MirrorCommand = [f"mirror2{Config.CMD_SUFFIX}", f"m2{Config.CMD_SUFFIX}"]
        self.QbMirrorCommand = [f"qbmirror2{Config.CMD_SUFFIX}", f"qm2{Config.CMD_SUFFIX}"]
        self.JdMirrorCommand = [f"jdmirror2{Config.CMD_SUFFIX}", f"jm2{Config.CMD_SUFFIX}"]
        self.YtdlCommand = [f"ytdl2{Config.CMD_SUFFIX}", f"y2{Config.CMD_SUFFIX}"]
        self.NzbMirrorCommand = [f"nzbmirror2{Config.CMD_SUFFIX}", f"nm2{Config.CMD_SUFFIX}"]
        self.LeechCommand = [f"leech2{Config.CMD_SUFFIX}", f"l2{Config.CMD_SUFFIX}"]
        self.QbLeechCommand = [f"qbleech2{Config.CMD_SUFFIX}", f"ql2{Config.CMD_SUFFIX}"]
        self.JdLeechCommand = [f"jdLeech2{Config.CMD_SUFFIX}", f"jl2{Config.CMD_SUFFIX}"]
        self.YtdlLeechCommand = [f"ytdlleech2{Config.CMD_SUFFIX}", f"yl2{Config.CMD_SUFFIX}"]
        self.NzbLeechCommand = [f"nzbleech2{Config.CMD_SUFFIX}", f"nl2{Config.CMD_SUFFIX}"]
        self.CloneCommand = f"clone2{Config.CMD_SUFFIX}"
        self.CountCommand = f"count2{Config.CMD_SUFFIX}"
        self.DeleteCommand = f"del2{Config.CMD_SUFFIX}"
        self.CancelTaskCommand = [f"cancel2{Config.CMD_SUFFIX}", f"c2{Config.CMD_SUFFIX}"]
        self.CancelAllCommand = f"cancelall2{Config.CMD_SUFFIX}"
        self.ForceStartCommand = [f"forcestart2{Config.CMD_SUFFIX}", f"fs2{Config.CMD_SUFFIX}"]
        self.ListCommand = f"list2{Config.CMD_SUFFIX}"
        self.SearchCommand = f"search2{Config.CMD_SUFFIX}"
        self.StatusCommand = f"status2{Config.CMD_SUFFIX}"
        self.UsersCommand = f"users2{Config.CMD_SUFFIX}"
        self.AuthorizeCommand = f"authorize2{Config.CMD_SUFFIX}"
        self.UnAuthorizeCommand = f"unauthorize2{Config.CMD_SUFFIX}"
        self.AddSudoCommand = f"addsudo2{Config.CMD_SUFFIX}"
        self.RmSudoCommand = f"rmsudo2{Config.CMD_SUFFIX}"
        self.PingCommand = f"ping2{Config.CMD_SUFFIX}"
        self.RestartCommand = f"restart2{Config.CMD_SUFFIX}"
        self.RestartSessionsCommand = f"restartses2{Config.CMD_SUFFIX}"
        self.StatsCommand = f"stats2{Config.CMD_SUFFIX}"
        self.HelpCommand = f"help2{Config.CMD_SUFFIX}"
        self.LogCommand = f"log2{Config.CMD_SUFFIX}"
        self.ShellCommand = f"shell2{Config.CMD_SUFFIX}"
        self.AExecCommand = f"aexec2{Config.CMD_SUFFIX}"
        self.ExecCommand = f"exec2{Config.CMD_SUFFIX}"
        self.ClearLocalsCommand = f"clearlocals2{Config.CMD_SUFFIX}"
        self.BotSetCommand = [f"bsetting2{Config.CMD_SUFFIX}", f"bs2{Config.CMD_SUFFIX}"]
        self.UserSetCommand = [f"usetting2{Config.CMD_SUFFIX}", f"us2{Config.CMD_SUFFIX}"]
        self.SelectCommand = f"sel2{Config.CMD_SUFFIX}"
        self.RssCommand = f"rss2{Config.CMD_SUFFIX}"


BotCommands = _BotCommands()
