#include "contiki.h"
#include "coap-engine.h"
#include "dev/leds.h"

#include <string.h>

/* Log configuration */
#include "sys/log.h"
#define LOG_MODULE "App"
#define LOG_LEVEL LOG_LEVEL_APP

static void res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset);

/* A simple actuator example, depending on the color query parameter and post variable mode, corresponding led is activated or deactivated */
RESOURCE(res_cooling,
         "title=\"LEDs: ?color=r|g|y, POST/PUT mode=on|off\";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
		char msg[50];
	    	memset(msg, 0, 50);
		sprintf(msg, "Response from actuator!");
		int length=sizeof(msg);
		coap_set_header_content_format(response, TEXT_PLAIN);
		coap_set_header_etag(response, (uint8_t *)&length, 1);
		coap_set_payload(response, msg, length);
		coap_set_status_code(response, CHANGED_2_04);
}
