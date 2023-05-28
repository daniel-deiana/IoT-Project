#include "contiki.h"
#include "coap-engine.h"
#include "dev/leds.h"

#include <string.h>

/* Log configuration */
#include "sys/log.h"
#define LOG_MODULE "App"
#define LOG_LEVEL LOG_LEVEL_APP
static int status = 0;

static void res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset);

/* A simple actuator example, depending on the color query parameter and post variable mode, corresponding led is activated or deactivated */
RESOURCE(res_cooling,
         "title=\"LEDs:?action=activate|deactivate\";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
	
  const char *action = NULL;
	coap_get_post_variable(request, "action", &action);
	coap_set_status_code(response, CHANGED_2_04);

	if (strcmp(action, "activate") == 0 && status = 0) {
		leds_set(LEDS_YELLOW);
		status = 1;
	}
	else if (strcmp(action, "deactivate") == 0 && status == 1){
		leds_set(LEDS_RED);
		status = 0;
	}
	else {
		printf("Actuator - action not allowed \n");
		coap_set_status_code(response, BAD_REQUEST_4_00);
	}
}
