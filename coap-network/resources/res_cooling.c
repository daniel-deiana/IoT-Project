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
RESOURCE(res_leds,
         "title=\"LEDs: ?color=r|g|y, POST/PUT mode=on|off\";rt=\"Control\"",
         NULL,
         res_post_put_handler,
         res_post_put_handler,
         NULL);

static void
res_post_put_handler(coap_message_t *request, coap_message_t *response, uint8_t *buffer, uint16_t preferred_size, int32_t *offset)
{
  printf("test - command");
}
