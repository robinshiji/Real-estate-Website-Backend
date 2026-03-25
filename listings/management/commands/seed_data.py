from django.core.management.base import BaseCommand
from listings.models import Property

class Command(BaseCommand):
    help = 'Seeds the database with initial property data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Property.objects.all().delete()

        # Initial data from properties.ts
        properties_data = [
            # ... (data keeps the same structure for now, but we just ignore agent) ...
            {
                "id": "villa-azure-reflections",
                "badge": "Waterfront",
                "status": "Available",
                "location": "Monaco • Mediterranean Coast",
                "city": "Monaco",
                "name": "Villa Azure Reflections",
                "price": "$32,500,000",
                "priceNote": "USD • Private Listing",
                "beds": 7,
                "baths": 9,
                "sqft": "12,400",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuB1_PNJvyjFWH1RPaEx8GHnjTmGUR6f84XpNCzfI_N44Hm7V3WJcIbZmUZmEseIUH8RYvjZxd7UbzABiFbp7PmUnajoOvSCBYKFML8kbogVwZIf0f_HL1zjKgHSKzqioAGED7d9iO2awO-i3h-pm3tT_1t6y0p7X9mFCTHGr1Df9eS_oXQNcXOamTjxUyYp5a_eh6PQOM4it1A2ZEted8ntwFyfSsWUKYlYrGdDZN8zTtqJ6rgY-DkXfTiLIbz0GOxqkk5JGYbcJfw",
                "description": "Perched above the glittering waters of the Mediterranean, Villa Azure Reflections is a masterwork of contemporary architecture. Floor-to-ceiling glass dissolves the boundary between interior and the infinite sea, while bespoke finishes — Calacatta marble, bronze detailing, and hand-woven textiles — create an atmosphere of understated opulence. The cascading infinity pool seems to pour directly into the horizon.",
                "features": [
                    "Infinity Edge Pool", "Private Beach Access", "Home Cinema", "Smart Home System",
                    "Yacht Mooring", "Wine Cellar", "Staff Quarters", "Panoramic Roof Terrace"
                ],
                "gallery": [
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuB1_PNJvyjFWH1RPaEx8GHnjTmGUR6f84XpNCzfI_N44Hm7V3WJcIbZmUZmEseIUH8RYvjZxd7UbzABiFbp7PmUnajoOvSCBYKFML8kbogVwZIf0f_HL1zjKgHSKzqioAGED7d9iO2awO-i3h-pm3tT_1t6y0p7X9mFCTHGr1Df9eS_oXQNcXOamTjxUyYp5a_eh6PQOM4it1A2ZEted8ntwFyfSsWUKYlYrGdDZN8zTtqJ6rgY-DkXfTiLIbz0GOxqkk5JGYbcJfw",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuASgMEOvKbH8gBvMUr4pQvKq6qMvIo_p6Vjz3Y8LFfDE61zrGhSuLFA4LRD1HgJnFlsW56CdLjr8iC0LonRri_FTvV9vFYE9XP5viFWHqk6AxCRTFov2EIMz5UQgBBnNWzKaxpo231UNNGA9dVS4phFWKnfQFyF2XBrars1DlSuCIXSyRbdwSjxVOxLMwXLL380UYZdLFYJRj4usM-nMnlgsWyi-Ij0tKnjFnyu_KZ5wRn_2QkkWMDzKVVCpmQnTpwHmjLOWknKoq8",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuA46kMEtOn_NHjxqWAuVLLmBQ21VBJ4IRd1O_Ny59g0G0u-NItfa3VPLDlF5YU_mALSZwF5bA1xBdoBDoKXUSV2GLbo7JGf6NXFHIDIn8_fr4T69I-oLkqm_ohr0limJnWT7c2k1rll1mE3B-DxhGsrWWfwld3oljuHcm1W6pSTgg_20VIMCbkZ1GDHW6_c-JLRN76-keduIIQOWU96gMMudX-Xo3lA2ks-Foyr1OCwXQNS-PvaYNSp8igloVkRb7bXfp6YVPvFx4w"
                ],
                "agent": {
                    "name": "Elena Rossi",
                    "title": "Global Luxury Specialist",
                    "phone": "+1 (310) 555-0192",
                    "email": "elena.rossi@atlivingspaces.com",
                    "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuCrhoAA7CWfKzmSIkZXj7qF-72MJaBkEdaZihdTGvJ61OZkBwPjuqvTXb1ZxmXnT5MOLh5mQlmDZqMGX5y_Oavwy-d86h0PcdUGGHMMJdHz6IuybAHR0A1_iMOHpMp5JPlFphX_Y_yB16xKrocvHZDOH1iLNTTbwvjhK1JODsCeJQ3UpL3wRZ4E-vgwYrZHfJyC3AD2jQ--pXTyMfmcQrU3nl_wCQaSYdvpn9RQ6gK838jJ3vsNF6Zaf3fSjtWQnfAIDNe-B30nojU"
                }
            },
            {
                "id": "obsidian-chalet",
                "status": "Available",
                "location": "Aspen • Colorado",
                "city": "Aspen",
                "name": "The Obsidian Chalet",
                "price": "$18,750,000",
                "priceNote": "USD • Private Listing",
                "beds": 5,
                "baths": 6,
                "sqft": "8,200",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuASgMEOvKbH8gBvMUr4pQvKq6qMvIo_p6Vjz3Y8LFfDE61zrGhSuLFA4LRD1HgJnFlsW56CdLjr8iC0LonRri_FTvV9vFYE9XP5viFWHqk6AxCRTFov2EIMz5UQgBBnNWzKaxpo231UNNGA9dVS4phFWKnfQFyF2XBrars1DlSuCIXSyRbdwSjxVOxLMwXLL380UYZdLFYJRj4usM-nMnlgsWyi-Ij0tKnjFnyu_KZ5wRn_2QkkWMDzKVVCpmQnTpwHmjLOWknKoq8",
                "description": "Dramatically carved into the mountainside, The Obsidian Chalet commands sweeping views over Aspen's most celebrated ski slopes. Anchored by volcanic stone and weathered timber, the interiors achieve a rare warmth — heated travertine floors, custom fireplaces, and triple-aspect windows that frame winter panoramas like living art.",
                "features": [
                    "Ski-in / Ski-out Access", "Heated Outdoor Pool & Spa", "Private Gym", "Chef's Kitchen",
                    "Home Theater", "Four-Car Heated Garage", "Sauna & Steam Room", "Mountain View Terraces"
                ],
                "gallery": [
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuASgMEOvKbH8gBvMUr4pQvKq6qMvIo_p6Vjz3Y8LFfDE61zrGhSuLFA4LRD1HgJnFlsW56CdLjr8iC0LonRri_FTvV9vFYE9XP5viFWHqk6AxCRTFov2EIMz5UQgBBnNWzKaxpo231UNNGA9dVS4phFWKnfQFyF2XBrars1DlSuCIXSyRbdwSjxVOxLMwXLL380UYZdLFYJRj4usM-nMnlgsWyi-Ij0tKnjFnyu_KZ5wRn_2QkkWMDzKVVCpmQnTpwHmjLOWknKoq8",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuB1_PNJvyjFWH1RPaEx8GHnjTmGUR6f84XpNCzfI_N44Hm7V3WJcIbZmUZmEseIUH8RYvjZxd7UbzABiFbp7PmUnajoOvSCBYKFML8kbogVwZIf0f_HL1zjKgHSKzqioAGED7d9iO2awO-i3h-pm3tT_1t6y0p7X9mFCTHGr1Df9eS_oXQNcXOamTjxUyYp5a_eh6PQOM4it1A2ZEted8ntwFyfSsWUKYlYrGdDZN8zTtqJ6rgY-DkXfTiLIbz0GOxqkk5JGYbcJfw"
                ],
                "agent": {
                    "name": "Marcus Sterling",
                    "title": "Principal Advisor, Americas",
                    "phone": "+1 (212) 555-0188",
                    "email": "marcus.sterling@atlivingspaces.com",
                    "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuCWEfMw1mVI4azcqKjSGD9yhT2iL2xqhwDFFgi4Lf1IFhugQYQZ5jpqkY11wEp3mBV27DkewPtWPj1n5XZbD7v39MO_wMJHKEAk-ZXpX6IhF98-KMfGXKsxBYQVjqrAQ0-o9qNQXJx67BSUkUfp_NWVDXbScswB8NA6jzcwi68okOnd3BQe0n9Li2anUk3cfDRhboq3kQuE70nPTfEPicrphHXA9ZSF2oIm18R9k-b8dTZKCwJMh36XlysgCkQxur_6QN7a-dqK3eE"
                }
            },
            {
                "id": "castello-di-marmo",
                "status": "Available",
                "location": "Tuscany • Italy",
                "city": "Tuscany",
                "name": "Castello di Marmo",
                "price": "$12,200,000",
                "priceNote": "USD • Historic Estate",
                "beds": 12,
                "baths": 10,
                "sqft": "24,000",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuA46kMEtOn_NHjxqWAuVLLmBQ21VBJ4IRd1O_Ny59g0G0u-NItfa3VPLDlF5YU_mALSZwF5bA1xBdoBDoKXUSV2GLbo7JGf6NXFHIDIn8_fr4T69I-oLkqm_ohr0limJnWT7c2k1rll1mE3B-DxhGsrWWfwld3oljuHcm1W6pSTgg_20VIMCbkZ1GDHW6_c-JLRN76-keduIIQOWU96gMMudX-Xo3lA2ks-Foyr1OCwXQNS-PvaYNSp8igloVkRb7bXfp6YVPvFx4w",
                "description": "A monument to Tuscan grandeur, Castello di Marmo has presided over its vineyard hillside for more than four centuries. Recently restored to flawless condition by a celebrated Florentine atelier, the castello marries original frescoed ceilings and vaulted stone cellars with discreet modern amenities. The 12-hectare estate includes an organic vineyard, olive grove, and formal Italian gardens.",
                "features": [
                    "12-Hectare Estate", "Organic Vineyard & Olive Grove", "Frescoed Grand Ballroom",
                    "Historic Wine Cellar", "Formal Italian Gardens", "Heated Pool & Pool House",
                    "Fully Restored Chapel", "Caretaker Cottage"
                ],
                "gallery": [
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuA46kMEtOn_NHjxqWAuVLLmBQ21VBJ4IRd1O_Ny59g0G0u-NItfa3VPLDlF5YU_mALSZwF5bA1xBdoBDoKXUSV2GLbo7JGf6NXFHIDIn8_fr4T69I-oLkqm_ohr0limJnWT7c2k1rll1mE3B-DxhGsrWWfwld3oljuHcm1W6pSTgg_20VIMCbkZ1GDHW6_c-JLRN76-keduIIQOWU96gMMudX-Xo3lA2ks-Foyr1OCwXQNS-PvaYNSp8igloVkRb7bXfp6YVPvFx4w",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuB1_PNJvyjFWH1RPaEx8GHnjTmGUR6f84XpNCzfI_N44Hm7V3WJcIbZmUZmEseIUH8RYvjZxd7UbzABiFbp7PmUnajoOvSCBYKFML8kbogVwZIf0f_HL1zjKgHSKzqioAGED7d9iO2awO-i3h-pm3tT_1t6y0p7X9mFCTHGr1Df9eS_oXQNcXOamTjxUyYp5a_eh6PQOM4it1A2ZEted8ntwFyfSsWUKYlYrGdDZN8zTtqJ6rgY-DkXfTiLIbz0GOxqkk5JGYbcJfw"
                ],
                "agent": {
                    "name": "Julianne Vane",
                    "title": "Managing Director, Europe",
                    "phone": "+39 055 555 0181",
                    "email": "julianne.vane@atlivingspaces.com",
                    "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuCzQZBblaGtGE3wbMe9HvnNr3AhGXomyv0_OSip2ysOjp8s_0lb4wZquTTgCVTMfxtgSiBCpSVapKQfQJXxoUU-gLArdqPPfkmMgF5lYRkayb0OljexzRyrIe4ks2RWG6DWDOuTnh5TswZVpc6Sz15d4lDNPnha9orRUZXcmzToVpTIKYmMAcixete3NQf89IOoPEQGd1OtljW2gyDOcH9pboZ8V_BPgp8TxwmeskCOF0wL7PauLRabPzDt_vm0Ad0ou1sBfEMQuIc"
                }
            },
            {
                "id": "luminary-pavilion",
                "badge": "New Construction",
                "status": "Available",
                "location": "Beverly Hills • California",
                "city": "Beverly Hills",
                "name": "The Luminary Pavilion",
                "price": "$45,000,000",
                "priceNote": "USD • Signature Collection",
                "beds": 8,
                "baths": 11,
                "sqft": "18,500",
                "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAtrE4aS81gO5W4w_v5t1XOkqeD7NZQFm7cQZzf5LoEtKaAiJAbivgtvkBDrkhDXgtpd_L6UVv5h2lOmmh2AlI7pzG9Wh8QSo_Dvv_htKhuOGBuETp4USobdQvmV_DDFkjrl5EQhCL_vyXSqVpB_v4gDnpt4BA1yAOh0sq_JiOs0nftwm0SosXYHFnE-joivcRTxZ6UKfGq1JSbVAYDDv6Hrild75NqC5o-f0PCiAsVIOGuGcW0KdwgdQb1lg8egmSYXfx2xTffrDE",
                "description": "The Luminary Pavilion is a statement of pure architectural ambition. Conceived by a Pritzker Prize-winning firm, its signature floating cantilevered form appears to defy gravity above a floodlit infinity pool. The interior program — curated by a leading international design house — spans an IMAX-grade private cinema, a 2,000-bottle wine vault, a fully equipped wellness spa, and a rooftop entertaining pavilion where the city lights unfold below.",
                "features": [
                    "Infinity Pool & Lounge", "IMAX Private Cinema", "2,000-Bottle Wine Vault",
                    "Full Wellness Spa", "Rooftop Entertaining Pavilion", "4-Car Underground Garage",
                    "Smart Home by Crestron", "Private Chef's Kitchen"
                ],
                "gallery": [
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuAtrE4aS81gO5W4w_v5t1XOkqeD7NZQFm7cQZzf5LoEtKaAiJAbivgtvkBDrkhDXgtpd_L6UVv5h2lOmmh2AlI7pzG9Wh8QSo_Dvv_htKhuOGBuETp4USobdQvmV_DDFkjrl5EQhCL_vyXSqVpB_v4gDnpt4BA1yAOh0sq_JiOs0nftwm0SosXYHFnE-joivcRTxZ6UKfGq1JSbVAYDDv6Hrild75NqC5o-f0PCiAsVIOGuGcW0KdwgdQb1lg8egmSYXfx2xTffrDE",
                    "https://lh3.googleusercontent.com/aida-public/AB6AXuB1_PNJvyjFWH1RPaEx8GHnjTmGUR6f84XpNCzfI_N44Hm7V3WJcIbZmUZmEseIUH8RYvjZxd7UbzABiFbp7PmUnajoOvSCBYKFML8kbogVwZIf0f_HL1zjKgHSKzqioAGED7d9iO2awO-i3h-pm3tT_1t6y0p7X9mFCTHGr1Df9eS_oXQNcXOamTjxUyYp5a_eh6PQOM4it1A2ZEted8ntwFyfSsWUKYlYrGdDZN8zTtqJ6rgY-DkXfTiLIbz0GOxqkk5JGYbcJfw"
                ],
                "agent": {
                    "name": "David Chen",
                    "title": "Director of Private Sales",
                    "phone": "+1 (310) 555-0207",
                    "email": "david.chen@atlivingspaces.com",
                    "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuDbThTU-169ByrXaVA9DFJgzAzWap_G6TH9kXEXcgo6K-nY6xo61ZUg8eBeF-LLRGDCzzGi59JD7LTnQbxWPPJDaQzThB8XpiqIZIjbwMqd4a0_UU_7PMZqVUG2rWkIgKpYaY8KAldvQHj1HJLysXZEc8wNwEkT6HWj3Ij1uwIbm5DYMJEt1StIUyH3oR0BY6mvJUGrf53DVD5OzPTev1tPiGBh1YGlG2mnkJxb9-wvxd4W7SJ5cNDUpSleVN_jE4PcYfHgbHjupCc"
                }
            }
        ]

        for item in properties_data:
            item_slug = item.pop('id')
            item.pop('image', None)
            item.pop('gallery', None)
            item.pop('agent', None) # Remove agent data
            
            Property.objects.get_or_create(
                slug=item_slug,
                defaults=item
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
