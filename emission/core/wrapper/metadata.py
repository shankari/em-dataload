import logging
import datetime as pydt
import pytz
import time

import emission.core.wrapper.wrapperbase as ecwb

class Metadata(ecwb.WrapperBase):
  props = {"key": ecwb.WrapperBase.Access.WORM,
           "platform": ecwb.WrapperBase.Access.WORM,
           "type": ecwb.WrapperBase.Access.WORM,
           "write_ts": ecwb.WrapperBase.Access.WORM,
           "write_local_dt": ecwb.WrapperBase.Access.WORM,
           "time_zone": ecwb.WrapperBase.Access.WORM,
           "write_fmt_time": ecwb.WrapperBase.Access.WORM,
           "read_ts": ecwb.WrapperBase.Access.WORM}

  enums = {}
  geojson = []
  nullable = []
  local_dates = ['write_local_dt']

  def _populateDependencies(self):
    pass

  @staticmethod
  def create_metadata_for_result(key):
      import emission.storage.decorations.local_date_queries as esdl
      import arrow

      m = Metadata()
      m.key = key
      m.platform = "server"
      m.write_ts = time.time()
      m.time_zone = "America/Los_Angeles"
      m.write_local_dt = esdl.get_local_date(m.write_ts, m.time_zone)
      m.write_fmt_time = arrow.get(m.write_ts).to(m.time_zone).isoformat()
      return m

  def isAndroid(self):
    return self.platform == "android"

  def isIOS(self):
    return self.platform == "ios"
