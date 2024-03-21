	// Geolocation API
		function getLocation() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(function(position) {
					showPosition(position);
					showConnectionState();
					showBatteryStatus();
					showProcessorCores();
					showDeviceMemory();
					showMaximumTouchPoints();
				});
			} else {
				alert("Geolocation is not supported by this browser.");
			}
		}

		function showPosition(position) {
			var latitude = position.coords.latitude;
			var longitude = position.coords.longitude;
			document.getElementById("location").innerHTML = "Latitude: " + latitude + "<br>Longitude: " + longitude;
		}

		// Connection State and Network Information API
	function showConnectionState() {
    var onlineStatus = navigator.onLine ? "Online" : "Offline";
    var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    var connectionType = connection ? connection.type : "Unknown";
    var effectiveType = connection && connection.effectiveType ? connection.effectiveType : "Unknown";
    document.getElementById("connection-state").innerHTML = "Connection state: " + onlineStatus + "<br>Connection type: " + connectionType + "<br>Effective network type: " + effectiveType;
}


		// Battery Status API
		function showBatteryStatus() {
			if (navigator.getBattery) {
				navigator.getBattery().then(function(battery) {
					var level = battery.level * 100;
					var charging = battery.charging ? "Yes" : "No";
					document.getElementById("battery-status").innerHTML = "Battery level: " + level + "%<br>Charging: " + charging;
				});
			} else {
				document.getElementById("battery-status").innerHTML = "Battery status not supported by this browser.";
			}
		}

		// Processor Cores API
		function showProcessorCores() {
			var cores = navigator.hardwareConcurrency || "Unknown";
			document.getElementById("processor-cores").innerHTML = "Number of processor cores: " + cores;
		}

		// Device Memory API
		function showDeviceMemory() {
			var memory = navigator.deviceMemory || "Unknown";
			document.getElementById("device-memory").innerHTML = "Device memory: " + memory + " GB";
		}

		// Maximum Touch Points API
		function showMaximumTouchPoints() {
			var points = navigator.maxTouchPoints || "Unknown";
			document.getElementById("maximum-touch-points").innerHTML = "Maximum touch points: " + points;
		}