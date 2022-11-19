"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TIME_WEEKS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from datetime import date

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([CalendarWeekSensor()])

class CalendarWeekSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Calendar Week"
    _attr_native_unit_of_measurement = TIME_WEEKS
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        
        week = date.today().strftime("%W")
        
        self._attr_native_value = week

    
