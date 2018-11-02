# Leviton Cloud Services API model Area.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Area(BaseModel):
    def __init__(self, session, model_id=None):
        super(Area, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/count"
        return session.call_api(api, attribs, 'get')

    def count_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_area_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_loads(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_sensors(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_shades(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_thermostat_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas"
        return session.call_api(api, attribs, 'post')

    def create_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_area_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_loads(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas"
        return session.call_api(api, attribs, 'post')

    def create_sensors(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_shades(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_thermostat_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_area_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_loads(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_sensors(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_shades(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_thermostat_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_area_snapshots(self, area_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots/{1}".format(self._id, area_snapshot_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_loads(self, load_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads/{1}".format(self._id, load_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_sensors(self, sensor_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors/{1}".format(self._id, sensor_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_shades(self, shade_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades/{1}".format(self._id, shade_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_thermostat_snapshots(self, thermostat_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots/{1}".format(self._id, thermostat_snapshot_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_thermostats(self, thermostat_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = Area(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        data = self._session.call_api(api, attribs, 'get')

        from .activity_trigger import ActivityTrigger
        model = ActivityTrigger(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_area_snapshots(self, area_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots/{1}".format(self._id, area_snapshot_id)
        data = self._session.call_api(api, attribs, 'get')

        from .area_snapshot import AreaSnapshot
        model = AreaSnapshot(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        data = self._session.call_api(api, attribs, 'get')

        from .load_snapshot import LoadSnapshot
        model = LoadSnapshot(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_loads(self, load_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads/{1}".format(self._id, load_id)
        data = self._session.call_api(api, attribs, 'get')

        from .load import Load
        model = Load(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_sensors(self, sensor_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors/{1}".format(self._id, sensor_id)
        data = self._session.call_api(api, attribs, 'get')

        from .sensor import Sensor
        model = Sensor(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_shades(self, shade_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades/{1}".format(self._id, shade_id)
        data = self._session.call_api(api, attribs, 'get')

        from .shade import Shade
        model = Shade(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_thermostat_snapshots(self, thermostat_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots/{1}".format(self._id, thermostat_snapshot_id)
        data = self._session.call_api(api, attribs, 'get')

        from .thermostat_snapshot import ThermostatSnapshot
        model = ThermostatSnapshot(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_thermostats(self, thermostat_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat_id)
        data = self._session.call_api(api, attribs, 'get')

        from .thermostat import Thermostat
        model = Thermostat(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Areas/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_activity_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .activity_trigger import ActivityTrigger
        result = []
        if items is not None:
            for data in items:
                model = ActivityTrigger(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_area_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .area_snapshot import AreaSnapshot
        result = []
        if items is not None:
            for data in items:
                model = AreaSnapshot(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/installation".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .installation import Installation
        model = Installation(self._session, data['id'])
        model.data = data
        return model

    def get_load_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .load_snapshot import LoadSnapshot
        result = []
        if items is not None:
            for data in items:
                model = LoadSnapshot(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_loads(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .load import Load
        result = []
        if items is not None:
            for data in items:
                model = Load(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_sensors(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .sensor import Sensor
        result = []
        if items is not None:
            for data in items:
                model = Sensor(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_shades(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .shade import Shade
        result = []
        if items is not None:
            for data in items:
                model = Shade(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_thermostat_snapshots(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .thermostat_snapshot import ThermostatSnapshot
        result = []
        if items is not None:
            for data in items:
                model = ThermostatSnapshot(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .thermostat import Thermostat
        result = []
        if items is not None:
            for data in items:
                model = Thermostat(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_activity_triggers(self, activity_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/activityTriggers/{1}".format(self._id, activity_trigger_id)
        data = self._session.call_api(api, attribs, 'put')

        from .activity_trigger import ActivityTrigger
        model = ActivityTrigger(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_area_snapshots(self, area_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/areaSnapshots/{1}".format(self._id, area_snapshot_id)
        data = self._session.call_api(api, attribs, 'put')

        from .area_snapshot import AreaSnapshot
        model = AreaSnapshot(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_load_snapshots(self, load_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loadSnapshots/{1}".format(self._id, load_snapshot_id)
        data = self._session.call_api(api, attribs, 'put')

        from .load_snapshot import LoadSnapshot
        model = LoadSnapshot(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_loads(self, load_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/loads/{1}".format(self._id, load_id)
        data = self._session.call_api(api, attribs, 'put')

        from .load import Load
        model = Load(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_sensors(self, sensor_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/sensors/{1}".format(self._id, sensor_id)
        data = self._session.call_api(api, attribs, 'put')

        from .sensor import Sensor
        model = Sensor(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_shades(self, shade_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/shades/{1}".format(self._id, shade_id)
        data = self._session.call_api(api, attribs, 'put')

        from .shade import Shade
        model = Shade(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_thermostat_snapshots(self, thermostat_snapshot_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostatSnapshots/{1}".format(self._id, thermostat_snapshot_id)
        data = self._session.call_api(api, attribs, 'put')

        from .thermostat_snapshot import ThermostatSnapshot
        model = ThermostatSnapshot(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_thermostats(self, thermostat_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat_id)
        data = self._session.call_api(api, attribs, 'put')

        from .thermostat import Thermostat
        model = Thermostat(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas"
        data = session.call_api(api, attribs, 'put')

        model = Area(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

