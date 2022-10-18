import config
from datetime import datetime
# def set_index_name(path, ip_addr='192.168.122.192', name_of_index='winlogbeat-automation-test'):

def set_index_name():
  s = datetime.now().strftime()
  dt_str = ''.join(c for c in s if c.isalnum())
  ip_addr = config.ip_addr
  name_of_index = "winlogbeat-" + config.index_name + dt_str
  path = config.path
  
  winlogbeat = f'''
  ###################### Winlogbeat Configuration Example ########################

  # This file is an example configuration file highlighting only the most common
  # options. The winlogbeat.reference.yml file from the same directory contains
  # all the supported options with more comments. You can use it as a reference.
  #
  # You can find the full configuration reference here:
  # https://www.elastic.co/guide/en/beats/winlogbeat/index.html

  # ======================== Winlogbeat specific options =========================

  # event_logs specifies a list of event logs to monitor as well as any
  # accompanying options. The YAML data type of event_logs is a list of
  # dictionaries.
  #
  # The supported keys are name, id, xml_query, tags, fields, fields_under_root,
  # forwarded, ignore_older, level, event_id, provider, and include_xml.
  # The xml_query key requires an id and must not be used with the name,
  # ignore_older, level, event_id, or provider keys. Please visit the
  # documentation for the complete details of each option.
  # https://go.es.io/WinlogbeatConfig

  winlogbeat.event_logs:
    - name: Application
      ignore_older: 72h

    - name: System

    - name: Security

    - name: ForwardedEvents
      tags: [forwarded]

    - name: Windows PowerShell
      event_id: 400, 403, 600, 800

    - name: Microsoft-Windows-PowerShell/Operational
      event_id: 4103, 4104, 4105, 4106

  # ====================== Elasticsearch template settings =======================

  setup.template.settings:
    index.number_of_shards: 1
    #index.codec: best_compression
    #_source.enabled: false

  setup.template.name: "winlogbeat-%{{[agent.version]}}"
  setup.template.pattern: "winlogbeat-%{{[agent.version]}}"

  # ================================== General ===================================

  # The name of the shipper that publishes the network data. It can be used to group
  # all the transactions sent by a single shipper in the web interface.
  #name:

  # The tags of the shipper are included in their own field with each
  # transaction published.
  #tags: ["service-X", "web-tier"]

  # Optional fields that you can specify to add additional information to the
  # output.
  #fields:
  #  env: staging

  # ================================= Dashboards =================================
  # These settings control loading the sample dashboards to the Kibana index. Loading
  # the dashboards is disabled by default and can be enabled either by setting the
  # options here or by using the `setup` command.
  #setup.dashboards.enabled: false

  # The URL from where to download the dashboards archive. By default this URL
  # has a value which is computed based on the Beat name and version. For released
  # versions, this URL points to the dashboard archive on the artifacts.elastic.co
  # website.
  #setup.dashboards.url:

  # =================================== Kibana ===================================

  # Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
  # This requires a Kibana endpoint configuration.
  setup.kibana:

    # Kibana Host
    # Scheme and port can be left out and will be set to the default (http and 5601)
    # In case you specify and additional path, the scheme is required: http://localhost:5601/path
    # IPv6 addresses should always be defined as: https://[2001:db8::1]:5601
    host: "{ip_addr}:5601"

    # Kibana Space ID
    # ID of the Kibana Space into which the dashboards should be loaded. By default,
    # the Default Space will be used.
    #space.id:

  # =============================== Elastic Cloud ================================

  # These settings simplify using Winlogbeat with the Elastic Cloud (https://cloud.elastic.co/).

  # The cloud.id setting overwrites the `output.elasticsearch.hosts` and
  # `setup.kibana.host` options.
  # You can find the `cloud.id` in the Elastic Cloud web UI.
  #cloud.id:

  # The cloud.auth setting overwrites the `output.elasticsearch.username` and
  # `output.elasticsearch.password` settings. The format is `<user>:<pass>`.
  #cloud.auth:

  # ================================== Outputs ===================================

  # Configure what output to use when sending the data collected by the beat.

  # ---------------------------- Elasticsearch Output ----------------------------
  output.elasticsearch:
    # Array of hosts to connect to.
    hosts: ["{ip_addr}:9200"]
    allow_older_versions: "true"
    index: "{name_of_index}"

    # Protocol - either `http` (default) or `https`.
    #protocol: "https"

    # Authentication credentials - either API key or username/password.
    #api_key: "id:api_key"
    #username: "elastic"
    #password: "changeme"

  # ------------------------------ Logstash Output -------------------------------
  #output.logstash:
    # The Logstash hosts
    #hosts: ["localhost:5044"]

    # Optional SSL. By default is off.
    # List of root certificates for HTTPS server verifications
    #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

    # Certificate for SSL client authentication
    #ssl.certificate: "/etc/pki/client/cert.pem"

    # Client Certificate Key
    #ssl.key: "/etc/pki/client/cert.key"

  # ================================= Processors =================================
  processors:
    - add_host_metadata:
        when.not.contains.tags: forwarded
    - add_cloud_metadata: ~ 

  # ================================== Logging ===================================

  # Sets log level. The default log level is info.
  # Available log levels are: error, warning, info, debug
  #logging.level: debug

  # At debug level, you can selectively enable logging only for some components.
  # To enable all selectors use ["*"]. Examples of other selectors are "beat",
  # "publisher", "service".
  #logging.selectors: ["*"]

  # ============================= X-Pack Monitoring ==============================
  # Winlogbeat can export internal metrics to a central Elasticsearch monitoring
  # cluster.  This requires xpack monitoring to be enabled in Elasticsearch.  The
  # reporting is disabled by default.

  # Set to true to enable the monitoring reporter.
  #monitoring.enabled: false

  # Sets the UUID of the Elasticsearch cluster under which monitoring data for this
  # Winlogbeat instance will appear in the Stack Monitoring UI. If output.elasticsearch
  # is enabled, the UUID is derived from the Elasticsearch cluster referenced by output.elasticsearch.
  #monitoring.cluster_uuid:

  # Uncomment to send the metrics to Elasticsearch. Most settings from the
  # Elasticsearch output are accepted here as well.
  # Note that the settings should point to your Elasticsearch *monitoring* cluster.
  # Any setting that is not set is automatically inherited from the Elasticsearch
  # output configuration, so if you have the Elasticsearch output configured such
  # that it is pointing to your Elasticsearch monitoring cluster, you can simply
  # uncomment the following line.
  #monitoring.elasticsearch:

  # ============================== Instrumentation ===============================

  # Instrumentation support for the winlogbeat.
  #instrumentation:
      # Set to true to enable instrumentation of winlogbeat.
      #enabled: false

      # Environment in which winlogbeat is running on (eg: staging, production, etc.)
      #environment: ""

      # APM Server hosts to report instrumentation results to.
      #hosts:
      #  - http://localhost:8200

      # API Key for the APM Server(s).
      # If api_key is set then secret_token will be ignored.
      #api_key:

      # Secret token for the APM Server(s).
      #secret_token:


  # ================================= Migration ==================================

  # This allows to enable 6.7 migration aliases
  #migration.6_to_7.enabled: true
  '''

  output_file = open(path + '\winlogbeat.yml', 'w')
  output_file.write(winlogbeat)
  output_file.close()
