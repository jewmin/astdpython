# -*- coding: utf-8 -*-
# 活动类型
from enum import Enum, unique


@unique
class ActivityType(Enum):
    HasArchEvent = 0
    WeekendGift = 1  # 登录礼包
    ShenHuo = 2  # 百炼精铁
    BaiShen = 3
    Yang = 4
    OfflineEvent = 5
    ArrestEvent = 6  # 抓捕活动
    GoldTicketEvent = 7
    YueBingEvent = 8
    BoatEvent = 9  # 龙舟
    BuffEvent = 10
    CuiLianEvent = 11  # 淬炼大放送
    PayHongBaoEvent = 12  # 充值送红包
    BGEvent = 13  # 大宴群雄
    QingMingEvent = 14  # 群雄煮酒
    DuanWuEvent = 15  # 百家宴
    MoonGeneralEvent = 16  # 赏月送礼
    TrainingEvent = 17  # 大练兵
    SnowTradingEvent = 18  # 雪地通商
    BombNianEvent = 19  # 抓年兽
    BorrowingArrowsEvent = 20  # 草船借箭
    ParadeEvent = 21  # 阅兵庆典
    TowerStage = 22  # 宝塔活动
    MoonTowerEvent = 23
    GoldBoxEvent = 24  # 群雄争霸
    NationDayGoldBoxEvent = 25  # 充值赠礼
    HasDayTreasureGame = 26
    HasTroopFeedback = 27
    HasCakeEvent = 28
    HasNationDayEvent = 29
    HasJailEvent = 30
    ShowKfYZ = 31
    ShowKfWD = 32  # 武斗会
    ShowKfPVP = 33  # 英雄帖
    RingEvent = 34  # 新年敲钟
    FeteEvent = 35  # 祭祀活动
    SuperFanPai = 36  # 超级翻牌
    DumpEvent = 37  # 宝石倾销
    GiftEventBaoShi4 = 38  # 宝石翻牌
    YuanDanQiFu = 39  # 酒神觉醒
    KfWDEventReward = 40  # 武斗庆典
    KfRank = 41  # 对战
    DoubleElevenEvent = 42  # 消费送礼
    GoldGiftType = 43  # 盛宴活动
    EatMoonCakeEvent = 44  # 中秋月饼
    SpringFestivalWishEvent = 45  # 许愿
    MemoryEvent = 46  # 新春拜年
