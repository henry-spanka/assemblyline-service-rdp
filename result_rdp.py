from assemblyline_v4_service.common.base import ServiceBase
from assemblyline_v4_service.common.request import ServiceRequest
from assemblyline_v4_service.common.result import Result, ResultSection, BODY_FORMAT
import json

class Rdp(ServiceBase):
    def __init__(self, config=None):
        super(Rdp, self).__init__(config)

    def start(self):
        # ==================================================================
        # Startup actions:
        #   Your service might have to do some warming up on startup to make things faster
        # ==================================================================

        self.log.info(f"start() from {self.service_attributes.name} service called")

    def execute(self, request: ServiceRequest) -> None:
        # ==================================================================
        # Execute a request:
        #   Every time your service receives a new file to scan, the execute function is called.
        #   This is where you should execute your processing code.
        #   For this example, we will only generate results ...
        # ==================================================================

        rdpUrl = self.config.get('rdpUrl', '').strip()

        if not rdpUrl:
            self.log.warning("No RDP URL configured, skipping RDP result generation.")
            return

        # 1. Create a result object where all the result sections will be saved to
        result = Result()

        # 2. Create a section to be displayed for this result
        url_section = ResultSection('CAPEv2 RDP', body_format=BODY_FORMAT.URL,
                                     body=json.dumps({"name": "RDP File", "url": rdpUrl}))

        # 3. Make sure you add your section to the result
        result.add_section(url_section)

        # 4. Wrap-up: Save your result object back into the request
        request.result = result
