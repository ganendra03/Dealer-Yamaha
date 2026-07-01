import re

contact_html = """<main class="main">
    <!-- Contact Section -->
    <section class="section" style="padding-top: 120px;">
      <div class="container section-title text-center mb-5" data-aos="fade-up">
        <h2 class="fw-bold" style="color: var(--heading-color);">Hubungi Dealer Yamaha</h2>
        <p class="text-muted">Punya pertanyaan seputar motor, simulasi kredit, atau booking servis? Silakan hubungi kami.</p>
      </div>

      <div class="container" data-aos="fade-up" data-aos-delay="100">
        <div class="row g-4 mb-5 justify-content-center">
          <div class="col-lg-4 col-md-6">
            <div class="card shadow-sm border-0 h-100 text-center py-5 rounded-4">
              <div class="card-body">
                <i class="bi bi-geo-alt-fill text-primary" style="font-size: 3rem; margin-bottom: 20px; display: inline-block;"></i>
                <h4 class="fw-bold">Alamat Dealer</h4>
                <p class="text-muted mb-0">Jl. Jenderal Sudirman No. 123<br>Jakarta Pusat, 10220</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="card shadow-sm border-0 h-100 text-center py-5 rounded-4">
              <div class="card-body">
                <i class="bi bi-telephone-fill text-primary" style="font-size: 3rem; margin-bottom: 20px; display: inline-block;"></i>
                <h4 class="fw-bold">Nomor Telepon</h4>
                <p class="text-muted mb-0">+62 812-3456-7890<br>Senin - Sabtu (08:00 - 17:00)</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="card shadow-sm border-0 h-100 text-center py-5 rounded-4">
              <div class="card-body">
                <i class="bi bi-envelope-fill text-primary" style="font-size: 3rem; margin-bottom: 20px; display: inline-block;"></i>
                <h4 class="fw-bold">Alamat Email</h4>
                <p class="text-muted mb-0">info@dealeryamaha.com<br>sales@dealeryamaha.com</p>
              </div>
            </div>
          </div>
        </div>

        <div class="row g-4 align-items-center">
          <div class="col-lg-6">
            <div class="card shadow-sm border-0 rounded-4 overflow-hidden h-100">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126920.24128522675!2d106.758832!3d-6.229728!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f3e945e34b9d%3A0x100c5e82dd4b820!2sJakarta!5e0!3m2!1sen!2sid!4v1700000000000!5m2!1sen!2sid" frameborder="0" style="border:0; width: 100%; min-height: 450px; height: 100%;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5">
              <h3 class="fw-bold mb-4">Kirim Pesan Langsung</h3>
              <form action="javascript:void(0);" onsubmit="window.location.href='https://wa.me/6281234567890?text=Halo%20Dealer%20Yamaha,%20saya%20punya%20pertanyaan'" class="row g-3">
                <div class="col-md-6">
                  <label for="name" class="form-label fw-semibold">Nama Lengkap</label>
                  <input type="text" class="form-control form-control-lg bg-light border-0" id="name" placeholder="Masukkan nama Anda" required>
                </div>
                <div class="col-md-6">
                  <label for="phone" class="form-label fw-semibold">Nomor WhatsApp</label>
                  <input type="tel" class="form-control form-control-lg bg-light border-0" id="phone" placeholder="0812xxxx" required>
                </div>
                <div class="col-12">
                  <label for="subject" class="form-label fw-semibold">Pilih Layanan</label>
                  <select class="form-select form-select-lg bg-light border-0" id="subject">
                    <option selected>Tanya Harga / Simulasi Kredit</option>
                    <option value="1">Booking Servis Bengkel</option>
                    <option value="2">Ketersediaan Suku Cadang (Sparepart)</option>
                    <option value="3">Informasi Promo</option>
                    <option value="4">Lainnya</option>
                  </select>
                </div>
                <div class="col-12">
                  <label for="message" class="form-label fw-semibold">Pesan Anda</label>
                  <textarea class="form-control form-control-lg bg-light border-0" id="message" rows="4" placeholder="Tulis pesan atau pertanyaan Anda di sini..."></textarea>
                </div>
                <div class="col-12 mt-4">
                  <button type="submit" class="btn btn-primary btn-lg w-100 rounded-pill"><i class="bi bi-whatsapp me-2"></i> Kirim via WhatsApp</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section><!-- /Contact Section -->
  </main>"""

with open("kontak.html", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(r'<main class="main">.*?</main>', contact_html, content, flags=re.DOTALL)

with open("kontak.html", "w", encoding="utf-8") as f:
    f.write(new_content)
