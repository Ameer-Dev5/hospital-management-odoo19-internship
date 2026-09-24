import {Component, onMounted, useState} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";

export class HospitalDashboard extends Component {
    static template = "hospital_base.HospitalDashboard";

    setup() {
        this.orm = useService("orm");
        this.actionService = useService("action");

        this.state = useState({
            patients: 0,
            appointments: 0,
            loading: true,
            error: false,
        });

        onMounted(() => {
            this.loadStatistics();
        });
    }

    async loadStatistics() {
        try {
            const [patients, appointments] = await Promise.all([
                this.orm.searchCount("hospital.patient", []),
                this.orm.searchCount("hospital.appointment", []),
            ]);

            this.state.patients = patients;
            this.state.appointments = appointments;
            this.state.error = false;
        } catch {
            this.state.error = true;
        } finally {
            this.state.loading = false;
        }
    }

    viewPatients() {
        this.actionService.doAction("hospital_base.action_hospital_patients");
    }

    viewAppointments() {
        this.actionService.doAction("hospital_base.action_hospital_appointment");
    }
}

registry.category("actions").add(
    "hospital_base.hospital_dashboard",
    HospitalDashboard,
);