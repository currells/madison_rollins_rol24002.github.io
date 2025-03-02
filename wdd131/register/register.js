        /*When the page loads set the current number of participants equal to 1
        Initialize a participant counter to 1.
        Add an event listener to the "Add Participant" button.
        When the button is clicked:
            1.Increment the participant counter.
            2.Create a copy of the participant HTML (<section class="participant1">).
            3.Modify the id attributes in the copied HTML to be unique (e.g., participant2, name2, etc.).
            4.Insert the new participant HTML before the "Add Participant" button.
        */
document.addEventListener('DOMContentLoaded', function() {
        //hide summary initially
        document.querySelector('#summary').style.display = 'none';

        //seting initial count
        let participantCount = 1;

        //participant count count=# of participancts
        function participantTemplate(count) {
            return
            function participantTemplate(count) {
                return `
                <section class="participant${count}">
                    <h3>Participant ${count}</h3>
                    <div class="item">
                    <label for="fname${count}">First Name<span>*</span></label>
                    <input id="fname${count}" type="text" name="fname${count}" required />
                    </div>
                    <div class="item activities">
                    <label for="activity${count}">Activity #<span>*</span></label>
                    <input id="activity${count}" type="text" name="activity${count}" />
                    </div>
                    <div class="item">
                    <label for="fee${count}">Fee ($)<span>*</span></label>
                    <input id="fee${count}" type="number" name="fee${count}" />
                    </div>
                    <div class="item">
                    <label for="date${count}">Desired Date <span>*</span></label>
                    <input id="date${count}" type="date" name="date${count}" />
                    </div>
                    <div class="item">
                    <p>Grade</p>
                    <select id="grade${count}" name="grade${count}">
                        <option selected disabled></option>
                        <option value="1">1st</option>
                        <option value="2">2nd</option>
                        <option value="3">3rd</option>
                        <option value="4">4th</option>
                        <option value="5">5th</option>
                        <option value="6">6th</option>
                        <option value="7">7th</option>
                        <option value="8">8th</option>
                        <option value="9">9th</option>
                        <option value="10">10th</option>
                        <option value="11">11th</option>
                        <option value="12">12th</option>
                    </select>
                    </div>
                </section>
                `;
            }

        // participanr listner??
        document.getElementById('add').addEventListener('click', function() {
            participantCount++;
            const newParticipantHTML = participantTemplate(participantCount);
            document.querySelector('.participants').insertBefore(document.createRange().createContextualFragment(newParticipantHTML), document.getElementById('add'));
        });


        //Function that creates new participant
        insertAdjacentHTML('beforebegin', newParticipantHTML)
            //create a new participant object
            let participant = {
                firstName: document.querySelector('#fname').value,
                activity: document.querySelector('#activity').value,
                fee: document.querySelector('#fee').value,
                date: document.querySelector('#date').value,
                grade: document.querySelector('#grade').value
            }
            //add the new participant to the participant array
            participants.push(participant);
            //increment the participant count
            count++;
            //create a new participant
            participantTemplate(count);

        //submit event nlistener
        document.querySelector('form').addEventListener('submit', function(event){
            //prevent the default action of the form
            event.preventDefault();
            //pulling the varibales froant he firm
            const adultName = document.getElementById('adult_name').value;
            const total = totalFees();
            //hiding form apon submission
            document.querySelector('form').style.display = 'none';
            //display the summary
            const summary = document.getElementById('summary');
        summary.innerHTML = `<h2>Hey ${adultName}! Your total is: ${total}</h2>`;
        summary.style.display = 'block';
        });
        
            //add up fees
            function totalFees() {
                let feeElements = document.querySelectorAll('[id^="fee"]');
                feeElements = [...feeElements];
                return feeElements.reduce((total, element) => {
                return total + parseFloat(element.value || 0);
                }, 0);
            }
});