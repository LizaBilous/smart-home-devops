import React from 'react';

function DeviceList({ devices, onToggle }) {
    return (
        <div>
            {devices.map(device => (
                <div key={device.id}>
                    <h3>{device.name}</h3>
                    <p>Статус: {device.status}</p>

                    <button onClick={() => onToggle(device.id)}>
                        Переключить
                    </button>
                </div>
            ))}
        </div>
    );
}

export default DeviceList;