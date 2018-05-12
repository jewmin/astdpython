# -*- coding: utf-8 -*-
# 通用任务
from logic.base_task import BaseTask
from logic.config import config


class CommonTask(BaseTask):
    def __init__(self):
        super(CommonTask, self).__init__()
        self.m_szName = "common"
        self.m_szReadable = "通用"

    def run(self):
        self.init()
        return self.next_half_hour()

    def init(self):
        misc_mgr = self.m_objServiceFactory.get_misc_mgr()
        city_mgr = self.m_objServiceFactory.get_city_mgr()
        misc_mgr.get_server_time()
        misc_mgr.get_player_info_by_user_id("")
        misc_mgr.get_extra_info()
        misc_mgr.get_player_extra_info2()
        city_mgr.get_main_city()

        # 登录奖励
        if config["mainCity"]["auto_get_login_reward"]:
            # 试试手气
            if self.m_objUser.m_bHasPerDayReward:
                city_mgr.get_per_day_reward()
            # 登录礼包
            city_mgr.get_new_gift_list()
            # 登录签到送礼
            city_mgr.get_login_reward_info()
            # 恭贺
            city_mgr.get_champion_info()

        # 将军塔
        if config["mainCity"]["auto_build_general_tower"]:
            city_mgr.get_general_tower_info()
