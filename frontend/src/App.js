import React, { useState, useEffect } from 'react';
import DeviceList from './DeviceList';

function App() {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/devices')
            .then(res => res.json())
            .then(data => setDevices(Object.values(data)));
    }, []);

    const toggleDevice = (deviceId) => {
        fetch(`http://localhost:8000/devices/${deviceId}/toggle`, {
            method: 'POST'
        })
            .then(res => res.json())
            .then(data => {
                setDevices(prevDevices =>
                    prevDevices.map(device =>
                        device.id === deviceId ? data.device : device
                    )
                );
            });
    };

    return (
        <div>
            <h1>Умный дом</h1>
            <DeviceList
                devices={devices}
                onToggle={toggleDevice}
            />
        </div>
    );
}

export default App;