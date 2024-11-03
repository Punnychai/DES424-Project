// Sample event data (could be replaced by API data)
const events = [
    { id: 1, name: 'Rock Fest 2024', date: '2024-05-15', location: 'Madison Square Garden' },
    { id: 2, name: 'Jazz Night', date: '2024-06-10', location: 'Blue Note Jazz Club' },
    { id: 3, name: 'Pop Extravaganza', date: '2024-07-20', location: 'Hollywood Bowl' }
];

// Load events on page
function loadEvents() {
    const eventList = document.getElementById('event-list');
    events.forEach(event => {
        const eventCard = document.createElement('div');
        eventCard.classList.add('col-md-4', 'mb-4');
        eventCard.innerHTML = `
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${event.name}</h5>
                    <p class="card-text">Date: ${event.date}</p>
                    <p class="card-text">Location: ${event.location}</p>
                    <button class="btn btn-primary" onclick="openBookingModal(${event.id})">Book Now</button>
                </div>
            </div>
        `;
        eventList.appendChild(eventCard);
    });
}

// Open booking modal and set event data
function openBookingModal(eventId) {
    const selectedEvent = events.find(event => event.id === eventId);
    document.getElementById('selectedEvent').value = selectedEvent.name;
    document.getElementById('bookingModalLabel').innerText = `Book for ${selectedEvent.name}`;
    $('#bookingModal').modal('show');
}

// Handle booking form submission
document.getElementById('bookingForm').addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Simulate booking success
    document.getElementById('bookingForm').style.display = 'none';
    document.getElementById('confirmationMessage').style.display = 'block';
    
    setTimeout(() => {
        $('#bookingModal').modal('hide');
        document.getElementById('bookingForm').reset();
        document.getElementById('bookingForm').style.display = 'block';
        document.getElementById('confirmationMessage').style.display = 'none';
    }, 3000); // Close modal after 3 seconds
});

// Load events when the page loads
document.addEventListener('DOMContentLoaded', loadEvents);
