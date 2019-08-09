from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement


class FeedPage(AppBasePage):
    """
        推荐页面
    """
    boot_ad = IdElement('com.vs.vipsai:id/btn_go')  # 启动页广告
    boot_ad_close_btn = IdElement('com.vs.vipsai:id/img_home_popu_close')  # 关闭广告
    feed_btn = XpathElement('(//android.widget.ImageView[@content-desc="唯赛"])[1]')  # 推荐
    join_btn = IdElement('com.vs.vipsai:id/nav_item_arena')  # 竞技场

    # def swipe(self, start_x, start_y, end_x, end_y, duration=None):
    #     """Swipe from one point to another point, for an optional duration.
    #
    #     :Args:
    #      - start_x - x-coordinate at which to start
    #      - start_y - y-coordinate at which to start
    #      - end_x - x-coordinate at which to stop
    #      - end_y - y-coordinate at which to stop
    #      - duration - (optional) time to take the swipe, in ms.
    #
    #     :Usage:
    #         driver.swipe(100, 100, 100, 400)
    #     """
    #     # `swipe` is something like press-wait-move_to-release, which the server
    #     # will translate into the correct action
    #     action = TouchAction(self)
    #     action \
    #         .press(x=start_x, y=start_y) \
    #         .wait(ms=duration) \
    #         .move_to(x=end_x, y=end_y) \
    #         .release()
    #     action.perform()
    #     return self
    #
    # def swipe_up(self):
    #     s = self.GetPageSize()
    #     sx = s[0] * 0.43
    #     sy = s[1] * 0.45
    #     ex = 0
    #     ey = s[1] * 0.55
    #     self.driver.swipe(sx, sy, ex, -ey, 100)

    # def swipe_up1(*args, t=100, n=1):
    #     """Swipe device screen up in t milliseconds and repeat the operation n times
    #            t=100 作为命名关键字参数 表示默认的滑动时间为100ms 可自寻设计滑动时间
    #            n=1 作为命名关键字参数 表示默认的滑动次数为1次 可自寻设计滑动次数
    #     """
    #     size = get_screen_size(*args)
    #     x1 = size[0] * 0.5
    #     y1 = size[1] * 0.75
    #     x2 = size[0] * 0.5
    #     y2 = size[1] * 0.25
    #     for i in range(n):
    #         if not args:
    #             os.system("adb shell input swipe %f %f %f %f %d" % (x1, y1, x2, y2, t))
    #         else:
    #             uid = args[0]
    #             os.system("adb -s %s shell input swipe %f %f %f %f %d" % (uid, x1, y1, x2, y2, t))

