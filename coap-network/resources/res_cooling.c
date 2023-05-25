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
         "title=\"LEDs:?action=activate|deactivate,POST/PUT mode=activate|deactivate\";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
	// set LED according to command 
    const char *action = NULL;
	coap_get_post_variable(request, "action", &action);
	//printf("the action variable sent is : %s\n",action);

	if (strcmp(action, "activate") == 0) {
		leds_set(LEDS_YELLOW);
		status = 1;
	}
	else if (strcmp(action, "deactivate") == 0 && status == 0){
		leds_set(LEDS_RED);
		status = 0;
	}
	else {
		printf("Actuator - action not allowed\n");
	}

	char msg[50];
	memset(msg, 0, 50);
	sprintf(msg, "Response from actuator!");
	//int length = sizeof(msg);
	//coap_set_header_content_format(response, TEXT_PLAIN);
	//coap_set_header_etag(response, (uint8_t *)&length, 1);
	//coap_set_payload(response, msg, length);
	coap_set_status_code(response, CHANGED_2_04);
}
